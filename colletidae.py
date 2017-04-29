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
        print( city_info["name"] )
        mounted_dictionary.append( city_info )
    writeCitiesWeatherDictToFile( mounted_dictionary )

def getCityInfoById(city_id):
    weather_api_url = "http://api.openweathermap.org/data/2.5/weather?id={}&appid={}".format(city_id, apidae_api_key)
    city_content = json.loads( requests.get(weather_api_url).content )
    return mountIndividualCityDict( city_content )

def mountIndividualCityDict(city_full_content):
    city_dict = {
        "name": city_full_content["name"],
        "coord": {
            "lat": city_full_content["coord"]["lat"],
            "lon": city_full_content["coord"]["lon"],
        },
        "main": {
            "temp": city_full_content["main"]["temp"],
            "pressure": city_full_content["main"]["pressure"],
            "humidity": city_full_content["main"]["humidity"],
            "temp_min": city_full_content["main"]["temp_min"],
            "temp_max": city_full_content["main"]["temp_max"]
        },
        "wind": {
            "speed": city_full_content["wind"]["speed"],
            "deg": city_full_content["wind"]["deg"] 
        }
    }

    return city_dict

def writeCitiesWeatherDictToFile(weather_dictionary):
    file = open('collected.txt', 'w')
    file.write( str(weather_dictionary) )


if __name__ == "__main__":
    main()