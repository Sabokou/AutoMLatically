from ml_framework.Preprocessing import Preprocessing
from ml_framework.ModelLoader import ModelLoader
from flask import Flask, request, send_file, Response
from flask_cors import CORS
import logging
import os
import json
from joblib import dump, load

PORT = 8001
# save the uploaded file into this directory inside the container
UPLOAD_DIR = "/uploaded_file"
DOWNLOAD_DIR = "/trained_models"

# ML Framework 
from ml_framework.ModelLoader import ModelLoader
from ml_framework.Preprocessing import Preprocessing
from ml_framework.ModelOptimizer import ModelOptimizer

loader = ModelLoader()
prepro = Preprocessing()
optimizer = ModelOptimizer()

app = Flask(__name__)

CORS(app, expose_headers=["Content-Disposition"])

# config
app.config['UPLOAD_FOLDER'] = "."


# Responses
def suc(message):
    return Response(message, status=200)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/upload", methods=['POST'])
def upload_file():
    app.logger.info(request.method)
    app.logger.info(request.files)
    if request.method == 'POST' and request.files:
        data_dir = os.path.join(UPLOAD_DIR, "data.csv")
        f = request.files['file']
        app.logger.info(f"Saving file {f}")
        f.save(data_dir)
        prepro.read_csv(data_dir)
    return suc('file uploaded successfully')


@app.route("/start", methods=['POST'])
def start_training():
    # TODO: delete this to fix the server side error 
    # content = json.dumps({"trained": ["tester"]})
    # return content

    if request.method == 'POST':
        app.logger.info(os.listdir(UPLOAD_DIR))
        # TODO: load the selected models
        trainingparams = request.get_json()
        models = trainingparams['selectedModels']
        goldLabel = trainingparams['gold_label']
        app.logger.info(f"These are the models: {models}")
        app.logger.info(f"This is the goldlable: {goldLabel}")

        # preprocess data
        # lin_data = prepro.linear_preprocessing()
        (X_train, X_test, y_train, y_test) = prepro.train_test_splitter(
            prepro.df, y_name=goldLabel)

        loader.load(model_names=models)
        loader.fit(X_train, y_train)
        app.logger.info(f"Y: {y_test}")
        loader.predict(X_test, y_test)

        # get best Model for hyperparameter tuning
        app.logger.info(f"Initial fits have ended. Optimizing best model {list(loader.best_model.keys())[0]} now.")
        tuned_model = optimizer.hyperparameter_optimize_single(model_name=list(loader.best_model.keys())[0],
                                                               model=list(loader.best_model.values())[0],
                                                               X=prepro.df.drop(goldLabel, axis="columns", inplace=False),
                                                               y=prepro.df[goldLabel])

        # Add score of finetuned model to score dict
        score = tuned_model.score(X_test, y_test)
        loader.scores["Fine-tuned " + list(loader.best_model.keys())[0]] = score

        # saves tuned model as best model
        dump(tuned_model, os.path.join(DOWNLOAD_DIR, "0_" + list(loader.best_model.keys())[0] + ".joblib"))
        # takes all currently trained and loaded models and sorts them by performance
        # takes all but the best model since it was tuned
        for cnt_item, item in enumerate(sorted(loader.scores.items(), key=lambda x: x[1])[1:]):
            dump(loader.models_dict.get(item[0]),
                 os.path.join(DOWNLOAD_DIR, str(cnt_item+1) + "_" + item[0] + '.joblib'))

        # content = json.loads(request.data)
        app.logger.info(f"{'Fine-tuned ' + list(loader.best_model.keys())[0]} with {tuned_model.get_params} achieved"
                        f" score of {score}")
        
        # send the names of the available trained models to the frontend
        resp = {"trained": list(loader.models_dict.keys())}
        app.logger.info(f"Response to the frontend: {resp}")
        return resp


@app.route("/performance", methods=['GET'])
def get_performance():
    if request.method == 'GET':
        # Current performance values (mean absolute error) are stored in loader's mae attribute
        scores = loader.scores

        # format model names to be more visually pleasing
        scores = {value[0].replace("_", " "): round(value[1], 3) for value in list(scores.items())}

        app.logger.info(
            f"You want to GET the /performance parameters\n. Current values:\n{scores}")

        return scores



@app.route("/model-names", methods=['GET'])
def get_model_names():
    if request.method == 'GET':
        app.logger.info(f"You want to GET the /model-names")
        avail_models = loader.get_available()
        content = json.dumps(avail_models)
        app.logger.info("Content", content)
        return suc(content)


@app.route("/download", methods=['GET', 'DELETE'])
def get_trained_models():
    """
    Accepted input to the GET method:
    {
        "model": "<name of model with underscores>",
        "top": <boolean>
    }
    If top is true the best model is downloaded.
    """
    if request.method == 'GET':
        requested_model = None
        try:
            app.logger.info(request.args)
            content = request.args
            #app.logger.info(f"You want to GET model {content}")
            if "model" in content:
                requested_model = content["model"]  
            elif "top" in content:
                requested_model = True
            app.logger.info(
                f"You want to request the model {requested_model}. If this sais true you get the best model.")
        except:
            return "The request is maleformed, make sure to format like this: { 'model': <model_name> } or {'top': true}"

        # search through the download dir for the requested saved model
        is_dir = os.path.exists(DOWNLOAD_DIR)
        app.logger.info(f"start walk, It is a dir: {is_dir}")
        if not is_dir:
            return f"Since the server container doesn't contain the folder '{DOWNLOAD_DIR}', there are no saved trained models, yet."

        # search through the saved files and store the file name without extension and path
        model_files = []
        for root, dirs, files in os.walk(DOWNLOAD_DIR):
            app.logger.info(f"Searching through files: {files}")
            for file in files:
                # remove the file extension
                name = file.split(".")[0]
                # absolute path to the file
                model_path = os.path.join(root, file)
                model_files.append( {"name": name, "name_full": file, "path": model_path} )

        # if a specific model name is provided send the model file that ends with that name 
        if isinstance(requested_model, str):
            for model_file in model_files:
                if model_file["name"].endswith(requested_model):
                    return send_file(model_file["path"], as_attachment=True, download_name=model_file["name_full"])
            return f"Could not find a model with the name '{requested_model}'"

        # if requested_model is "True" the best model (starting with 0) is sent
        elif isinstance(requested_model, bool) and requested_model:
            for model_file in model_files:
                if model_file["name"].startswith("0"):
                    return send_file(model_file["path"], as_attachment=True, download_name=model_file["name_full"])
            return "Could not find the best model which starts with '0'"


            # for root, dirs, files in os.walk(DOWNLOAD_DIR):
            #     app.logger.info(f"Searching through files: {files}")
            #     for file in files:
            #         # remove the file extension
            #         f_name = file.split(".")[0]
            #         # search for model by name
            #         if f_name.endswith(requested_model) and f_name.startswith("0"):
            #             app.logger.info(f"checking file {file}")
            #             model_path = os.path.join(root, file)
            #             app.logger.info(model_path)
            #             return send_file(model_path, as_attachment=True)
            #     return "Did not find the selected model"


    # remove all previously stored trained models
    elif request.method == 'DELETE':
        if os.path.exists(DOWNLOAD_DIR):
            # might fail if the folder exists but is empty
            try:
                for root, dirs, files in os.walk(DOWNLOAD_DIR):
                    for file in files:
                        os.remove(os.path.join(root, file))
                return suc("Folder content deleted")
            except:
                return suc("Folder already empty")
        # create the folder if it doesn't exist
        else:
            os.mkdir(DOWNLOAD_DIR)
            return suc("Folder is created and empty")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
