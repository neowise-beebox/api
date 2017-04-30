#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
from database import megachilidaeconnection

connection = megachilidaeconnection.getConnection()

## Implementar o id e o device_id
def newBee(beedata):
    return {
        "description": beedata["description"],
        "image_path": beedata["picture"],
        "species": beedata["species"],
        "coord": {
            "lat": beedata["latitude"],
            "lng": beedata["longitude"]
        }
    }

def save(beejson):
    print "sended data ==> {}".format( beejson )
    print "sended data type ==> {}".format(type( beejson ))
    connection.post( "/bees", newBee( json.loads(beejson) ) )

def listBeeOccurrences():
    bee_list = []
    results = connection.get( "/bees", None)
    for bee_key in results:
        bee_list.append( results[bee_key] )
    return bee_list