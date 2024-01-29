from tracemalloc import start
from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import  simPlayers as sp

from time import sleep
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# db = SQLAlchemy(app)

from datetime import datetime
from tokenize import _all_string_prefixes
from player_stat_metrics import get_top_player_dict

import json
from time import sleep


@app.route('/', methods=['POST', 'GET'])




def index():
    
    # p()
    sleep(1)
    global data
    print("run")
    if request.method == 'POST':
        team = json.loads(request.data)["team"]
        player_data = sp.load_prep_data("all_player_stats.csv")
        traded_player = int(get_top_player_dict()[team])
        ids = sp.get_player_ids(player_data, "2023-24", traded_player)
        
        data = {"teamData" : [sp.get_names(ids)]}
        
    elif request.method == 'GET' :
        return data

    return data



if __name__ == "__main__":
    app.run(debug=True)