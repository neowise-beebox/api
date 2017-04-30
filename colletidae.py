import json
import requests

apidae_api_key = "0079f159f4ced7bbe0694468132deee8"

def main():
    getCitiesInfo(320)

def getCitiesInfo(index):
    cities = open("new_list.txt").read().split(',')
    try:
        city_info = getCityInfoById( cities[index] )
        writeCitiesWeatherDictToFile( city_info )
        index+=1
        getCitiesInfo(index)
    except requests.exceptions.ConnectionError:
        getCitiesInfo(index)

def getCityInfoById(city_id):
    weather_api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_id, apidae_api_key)
    city_content = json.loads( requests.get(weather_api_url).content )
    print city_content["id"] if city_content.has_key("id") else "anony" 
    return mountIndividualCityDict( city_content )

def mountIndividualCityDict(city_full_content):
    city_dict = {
        "name": city_full_content["name"] if city_full_content.has_key("name") else "",
        "coord": {
            "lat": city_full_content["coord"]["lat"] if city_full_content["coord"].has_key("lat") else "",
            "lon": city_full_content["coord"]["lon"] if city_full_content["coord"].has_key("lon") else "",
        },
        "main": {
            "temp": city_full_content["main"]["temp"] if city_full_content["main"].has_key("temp") else "",
            "pressure": city_full_content["main"]["pressure"] if city_full_content["main"].has_key("pressure") else "",
            "humidity": city_full_content["main"]["humidity"] if city_full_content["main"].has_key("humidity") else "",
            "temp_min": city_full_content["main"]["temp_min"] if city_full_content["main"].has_key("temp_min") else "",
            "temp_max": city_full_content["main"]["temp_max"] if city_full_content["main"].has_key("temp_max") else ""
        },
        "wind": {
            "speed": city_full_content["wind"]["speed"] if city_full_content["wind"].has_key("speed") else "",
            "deg": city_full_content["wind"]["deg"] if city_full_content["wind"].has_key("deg") else ""
        }
    }

    return city_dict

def writeCitiesWeatherDictToFile(weather_dictionary):
    file = open('collected.txt', 'a+')
    file.write( str(weather_dictionary) + "\n" )


if __name__ == "__main__":
    main()