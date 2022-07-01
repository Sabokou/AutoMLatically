from flask import Flask, request
from flask_cors import CORS
import logging
import os
import json

PORT = 8001
# save the uploaded file into this directory inside the container
BASE_DIR = "/volume"

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
        f = request.files['file']
        app.logger.info(f"Saving file {f}")
        f.save(os.path.join(BASE_DIR, f.filename))
    return 'file uploaded successfully'

@app.route("/start", methods=['POST'])
def start_training():
    if request.method == 'POST':
        content = json.loads(request.data)
        app.logger.info(f"You posted the following /start parameters: {content}")
        return f"You requested /start with the content: {content}"

@app.route("/performance", methods=['GET'])
def get_perfromance():
    if request.method == 'GET':
        app.logger.info(f"You want to GET the /performance parameters")
        content = json.dumps({"nlpregressor": "0.1234"})
        return f"Your dummy performance is: {content}"

@app.route("/model-names", methods=['GET'])
def get_model_names():
    if request.method == 'GET':
        app.logger.info(f"You want to GET the /model-names")
        content = json.dumps({"modelNames": ["nlpregressor", "testclassifier"]})
        return f"Available ml-models are: {content}"
        
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)
