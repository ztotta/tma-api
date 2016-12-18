from flask import Flask
app = Flask(__name__)
from flask import render_template

import json
import os

# Welcome page with instructions:
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Loading the JSON file:	
with open('acronymsList.json') as json_data:
    d = json.loads(json_data.read())
    
# Searches database and responds with JSON:		
@app.route('/json/<abr>')
def abbreveJSON(abr=None):
    for i in range(0, len(d)): # Checks to see if the acronym/abbreviation is in the database:
        if d[i]['abbreve'] == abr or d[i]['abbreve'].lower() == abr or d[i]['abbreve'].upper() == abr:
            return json.dumps(d[i])
    else:
        return json.dumps(d[0]) # Responds with "TACNBF = That Acronym Can Not Be Found"

# Searches database and responds with HTML:				
@app.route('/<abr>')
def abbreve(abr=None):
    for i in range(0, len(d)): # Checks to see if the acronym/abbreviation is in the database:
        if d[i]['abbreve'] == abr or d[i]['abbreve'].lower() == abr or d[i]['abbreve'].upper() == abr:
            abr = d[i]['abbreve']
            mean = d[i]['meaning']
            answer = abr + " = " + mean
            return render_template('success.html', abr=answer)
    else:
        return render_template('failure.html') # Responds with failed search template:
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)