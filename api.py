import os
import json

from flask import Flask, jsonify, request

#import psycopg2

#config_data = {}
#with open("config.json", "r", encoding="utf-8") as json_file:
#    config_data = json.load(json_file)

#print(config_data)
#conn = psycopg2.connect("dbname={} user={} password={} host={}".format(config_data["db_name"], config_data["db_user"], config_data["db_password"], config_data["db_host"]))

import sys
app = Flask(__name__)

@app.route('/')
def index():
    # Primeira rota da API - Apresentação
    return jsonify({"name": "Dona Benta API", "version": "1.0.0"})

@app.route("/voice-command-input", methods=['POST'])
def input_vc():
    raw_data_speech = request.get_json()["message"]
    return {"response": raw_data_speech}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)