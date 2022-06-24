from flask import Flask, request
from flask_cors import CORS
import logging
import os 

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

@app.route("/upload", methods = ['POST'])
def upload_file():
    if request.method == 'POST' and request.files:
      f = request.files['file']
      app.logger.info(f"Saving file {f}")
      f.save(os.path.join(BASE_DIR, f.filename))
    return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT)