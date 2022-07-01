from flask import Flask, request
from flask_cors import CORS
import logging
import os
import json

PORT = 8001
# save the uploaded file into this directory inside the container
BASE_DIR = "/uploaded_file"

# ML Framework 
from ml_framework.ModelLoader import ModelLoader
from ml_framework.Preprocessing import Preprocessing
loader = ModelLoader()
prepro = Preprocessing()


app = Flask(__name__)
CORS(app)

# config
app.config['UPLOAD_FOLDER'] = "."


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST' and request.files:
        data_dir = os.path.join(BASE_DIR, "data.csv")
        f = request.files['file']
        app.logger.info(f"Saving file {f}")
        f.save(data_dir)
        prepro.read_csv(data_dir)
    return 'file uploaded successfully'

@app.route("/start", methods=['POST'])
def start_training():
    if request.method == 'POST':
        # TODO: load the selected models

        # preprocess data
        lin_data = prepro.linear_preprocessing()
        (X_train, X_test, y_train, y_test) = prepro.train_test_splitter(lin_data, y_name="Salary")
        
        # TODO: fit data to all models


        content = json.loads(request.data)
        app.logger.info(f"You posted the following /start parameters: {content}")
        return f"You requested /start with the content: {content}"

@app.route("/performance", methods=['GET'])
def get_performance():
    if request.method == 'GET':
        # TODO: calculate the performance using the training dataset
        #prediction_dict = loader.predict(X_test, y=y_test)
        #mae = loader.mae

        app.logger.info(f"You want to GET the /performance parameters")
        content = json.dumps({"nlpregressor": "0.1234"})
        return f"Your dummy performance is: {content}"

@app.route("/model-names", methods=['GET'])
def get_model_names():
    if request.method == 'GET':
        app.logger.info(f"You want to GET the /model-names")
        avail_models = loader.get_available()
        content = json.dumps(avail_models)
        return f"Available ml-models are: {content}"
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
