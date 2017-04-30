#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
from weatherhelper import weatherhelper
from database import megachilidaeconnection
from beeevaluator.beeevaluator import BeeEvaluator 

connection = megachilidaeconnection.getConnection()

def getRelativesCities():
    json_dump = json.loads( open("collected.txt", "r").read() )
    evaluate_list = []
    for x, dictionary in enumerate( json_dump ):
        if x == 5:
            break
        beeevaluator = BeeEvaluator(dictionary)
        beeevaluator.evaluate()
        evaluate_list.append(beeevaluator.getEvaluatedCity())
    sorted_list = sorted(evaluate_list, key=lambda k: k["score"])
    return sorted_list

## Implementar o id e o device_id
def newBee(beedata):
    weather_info = weatherhelper.getWeatherUsingCoord(beedata["latitude"], beedata["longitude"])

    data = {
        "description": beedata["description"],
        "image_path": beedata["picture"],
        "species": beedata["species"],
        "coord": {
            "lat": beedata["latitude"],
            "lng": beedata["longitude"]
        }
    }
    data.update(weather_info)
    return data

def save(beejson):
    result = connection.post("/bees", newBee( json.loads(beejson) ) )
    saveRelatives(result["name"])

def saveRelatives(node_id):
    connection.post("/relatives/{}".format(node_id), getRelativesCities())

def listBeeOccurrences():
    bee_list = []
    results = connection.get( "/bees", None)
    for bee_key in results:
        bee_list.append( results[bee_key] )
    return bee_list

def listRelativesByOccurrenceId(id):
    return connection.get("relatives", id)