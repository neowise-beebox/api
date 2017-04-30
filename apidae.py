#!/usr/local/bin python

from flask import Flask
from flask import jsonify
from flask import request
from database.dao import beedao

app = Flask( __name__ )

# Welcome to BeeBox
@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to BeeBox!"

# Creates new bee occurrence
@app.route("/savebee", methods=["POST"])
def savebee():
    print request.form["beedata"]
    beedao.save(request.form["beedata"])
    return jsonify( {"status": 200, "text": "bee saved"} )

# Lists all bee occurrences
@app.route("/listbee", methods=["GET"])
def listbees():
    return jsonify( beedao.listBeeOccurrences() )

if __name__ == '__main__':
    app.run(app.config['LISTEN_HOST'], app.config['LISTEN_PORT'])
