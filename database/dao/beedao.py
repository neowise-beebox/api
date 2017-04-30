#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
import pytemperature
from weatherhelper import weatherhelper
from database import megachilidaeconnection
from beeevaluator.beeevaluator import BeeEvaluator 

connection = megachilidaeconnection.getConnection()

def getRelativesCities(beesample):
    dump = json.loads( open("collected.txt", "r").read() )
    print beesample
    city_list = []
    for city in dump:
        city_score = beesample["weather"]["temp"] - pytemperature.k2c(city["weather"]["temp"]) + beesample["weather"]["humidity"] - city["weather"]["humidity"] + beesample["wind"]["speed"] - city["wind"]["speed"]
        city_list.append({
            "score": abs( round((city_score * 0.1), 3) ),
            "name": city["state"]
        })
    city_list = sorted( city_list, key=lambda key: key["score"] )
    return city_list[:5]

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
    beejson = json.loads(beejson)
    beename = "{}{}".format(beejson["idDevice"], beejson["cod"])
    weathered_bee = newBee( beejson )
    result = connection.patch("/bees/{}".format(beename), weathered_bee )
    saveRelatives(beename, weathered_bee)

def saveRelatives(node_id, beesample):
    connection.post("/relatives/{}".format(node_id), getRelativesCities(beesample))

def listBeeOccurrences():
    bee_list = []
    results = connection.get( "/bees", None)
    for bee_key in results:
        bee_list.append( results[bee_key] )
    return bee_list

def listRelativesByOccurrenceId(id):
    results = connection.get("relatives", id)
    for result in results:
        index = result
    return results.pop(index)
