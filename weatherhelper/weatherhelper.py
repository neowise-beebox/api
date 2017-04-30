#!usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests
import pytemperature

apidae_api_key = "0079f159f4ced7bbe0694468132deee8"

def getWeatherUsingCoord(lat, lng):
    weather_api_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lng, apidae_api_key)
    weather_info = requests.get( weather_api_url ).content
    return mount_dict(weather_info)

def mount_dict(info):
    info = json.loads(info)
    return {
        "state": info["name"] if info.has_key("name") else "",
        "weather": {
            "temp": pytemperature.k2c(info["main"]["temp"]) if info["main"].has_key("temp") else "",
            "pressure": info["main"]["pressure"] if info["main"].has_key("pressure") else "",
            "humidity": info["main"]["humidity"] if info["main"].has_key("humidity") else "",
            "max": pytemperature.k2c(info["main"]["temp_max"]) if info["main"].has_key("temp_max") else "",
            "min": pytemperature.k2c(info["main"]["temp_min"]) if info["main"].has_key("temp_min") else "",
        },
        "wind": {
            "speed": info["wind"]["speed"] if info["wind"].has_key("speed") else "",
            "deg": info["wind"]["deg"] if info["wind"].has_key("deg") else "",
        }
    }