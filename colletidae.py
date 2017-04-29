import json
import requests

apidae_api_key = "0079f159f4ced7bbe0694468132deee8"

def main():
    getCitiesInfo()

def getCitiesInfo():
    mounted_dictionary = []
    cities = json.loads( open("city.list.json").read() )
    for city in cities:
        city_info = getCityInfoById( city["id"] )
        writeCitiesWeatherDictToFile( city_info )
        mounted_dictionary.append( city_info )

def getCityInfoById(city_id):
    weather_api_url = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}".format(city_id, apidae_api_key)
    city_content = json.loads( requests.get(weather_api_url).content )
    print city_content["id"]
    return mountIndividualCityDict( city_content )

def mountIndividualCityDict(city_full_content):
    city_dict = {
        "name": city_full_content["name"],
        "coord": {
            "lat": city_full_content["coord"]["lat"],
            "lon": city_full_content["coord"]["lon"],
        },
        "main": {
            "temp": city_full_content["main"]["temp"] if city_full_content["main"].has_key("temp") else "",
            "pressure": city_full_content["main"]["pressure"] if city_full_content["main"].has_key("pressure") else "",
            "humidity": city_full_content["main"]["humidity"] if city_full_content["main"].has_key("humidity") else "",
            "temp_min": city_full_content["main"]["temp_min"] if city_full_content["main"].has_key("temp_min") else "",
            "temp_max": city_full_content["main"]["temp_max"] if city_full_content["main"].has_key("temp_max") else ""
        },
        "wind": {
            "speed": city_full_content["wind"]["speed"] if city_full_content["wind"]["speed"] else "",
            "deg": city_full_content["wind"]["deg"] if city_full_content["wind"]["deg"] else ""
        }
    }

    return city_dict

def writeCitiesWeatherDictToFile(weather_dictionary):
    file = open('collected.txt', 'a+')
    file.write( str(weather_dictionary) + "\n" )


if __name__ == "__main__":
    main()