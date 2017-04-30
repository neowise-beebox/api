#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
from database import megachilidaeconnection

connection = megachilidaeconnection.getConnection()

## Implementar o id e o device_id
def newBee(beedata):
    return {
        "description": beedata["description"],
        "image_path": beedata["image"],
        "coord": {
            "lat": beedata["lat"],
            "lng": beedata["lng"]
        }
    }

def save(beejson):
    connection.post( "/bees", newBee( json.loads( beejson ) ) )

def createBeeListForMap():
    beesdict = []
    occurrences = connection.get( "bees", None )
    for occurrence_index in occurrences:
        occurrence = occurrences[occurrence_index]
        beedict = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": {
                    occurrence["coord"]["lat"],
                    occurrence["coord"]["lng"]
                }                
            },
            "properties": {
                "description": occurrence[occurrence]["description"]   
            }
        }
        print beedict
        # beesdict.append(beedict)

def listBeeOccurrences():
    beesdict = {
        "type": "FeatureCollection",
        "features": []
    }
    createBeeListForMap()