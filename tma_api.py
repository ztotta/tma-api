from flask import Flask
app = Flask(__name__)
from flask import render_template

import json

@app.route('/')
def hello_world():
    return render_template('hello.html')

with open('acronymsList.json') as json_data:
    d = json.loads(json_data.read())
    
@app.route('/<abr>')
def abbreve(abr=None):
    for i in range(0, len(d)):
        if d[i]['abbreve'] == abr or d[i]['abbreve'].lower() == abr or d[i]['abbreve'].upper() == abr:
            abr = d[i]['abbreve']
            mean = d[i]['meaning']
            answer = abr + " = " + mean
            return render_template('success.html', abr=answer)
    else:
        return render_template('failure.html')