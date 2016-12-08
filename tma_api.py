from flask import Flask
app = Flask(__name__)
from flask import render_template

import json

@app.route('/')
def hello_world():
    return 'Hello, World!'

with open('acronymsList.json') as json_data:
    d = json.loads(json_data.read())
    
@app.route('/<query>')
def abbreve(query):
    for i in range(0, len(d)):
        if d[i]['abbreve'] == query or d[i]['abbreve'].lower() == query or d[i]['abbreve'].upper() == query:
            abr = d[i]['abbreve']
            mean = d[i]['meaning']
            return abr + " = " + mean
    else:
        return "Failure"