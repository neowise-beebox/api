#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
from weatherhelper import weatherhelper
from database import megachilidaeconnection

connection = megachilidaeconnection.getConnection()

## Implementar o id e o device_id
def newBee(beedata):
    # print weatherhelper.getWeatherUsingCoord(beedata["latitude"], beedata["longitude"])
    data = {
        "description": beedata["description"],
        "image_path": beedata["picture"],
        "species": beedata["species"],
        "coord": {
            "lat": beedata["latitude"],
            "lng": beedata["longitude"]
        }
    }
    data.update(weatherhelper.getWeatherUsingCoord(beedata["latitude"], beedata["longitude"]))
    return data

def save(beejson):
    connection.post("/bees", newBee( json.loads(beejson) ) )

def listBeeOccurrences():
    bee_list = []
    results = connection.get( "/bees", None)
    for bee_key in results:
        bee_list.append( results[bee_key] )
    return bee_list