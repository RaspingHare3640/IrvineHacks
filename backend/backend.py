from tracemalloc import start
from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from time import sleep
operator = "AceRail"
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

from datetime import datetime
from tokenize import _all_string_prefixes

import json
from time import sleep

data = {"team": "Hello"}
@app.route('/', methods=['POST', 'GET'])



def index():
    sleep(1)
    if request.method == 'POST':
        team = json.loads(request.data)["team"]
        data["team"] = team
    elif request.method == 'GET' :
        return data

    return data



if __name__ == "__main__":
    app.run(debug=True)