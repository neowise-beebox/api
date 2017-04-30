#!usr/bin/env python
#-*- coding: utf-8 -*-

from firebase import firebase

url_connection = "https://megachilidae-dbe05.firebaseio.com/"

# Retrieves firebase connection
def getConnection():
    return firebase.FirebaseApplication( url_connection )
