#!/usr/local/bin python

from flask import Flask
from flask import jsonify
from flask import request
from database.dao import beedao
from flask.ext.cors import CORS, cross_origin

app = Flask( __name__ )
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Welcome to BeeBox
@app.route("/", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def welcome():
    return "Welcome to BeeBox!"

# Creates new bee occurrence
@app.route("/savebee", methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def savebee():
    beedao.save(request.form["beedata"])
    return jsonify( {"status": 200, "text": "bee saved"} )

# Lists all bee occurrences
@app.route("/listbee", methods=["GET"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def listbees():
    return jsonify( beedao.listBeeOccurrences() )

if __name__ == '__main__':
    app.run()
    # app.run(app.config['LISTEN_HOST'], app.config['LISTEN_PORT'])
