from flask import Flask, jsonify
import json
from flask import request
from flask_cors import CORS
from os import path


app = Flask(__name__)
cors = CORS(app)
@app.route("/write", methods = ["POST"])
def write_json_file():
    data = request.data.decode('UTF-8')
    data = json.loads(data)
    print(data)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))
    return "<p>Wrote into json file</p>"

filename = '/Users/marantharodrigues/Documents/SYSC4907/test/backend/data.json'
listObj = []


@app.route("/")
def hello_world():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    response = jsonify(data)
    
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
