import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def weatherGetter(location):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"
    querystring = {"q": location, "units": "\"imperial\""}
    headers = {
        'x-rapidapi-key': "87e512e94fmshaf75e63e22d0ae6p11a488jsn0cadbfcac69c",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    jprint(response.json())


while True:
    location = str(
        input("Please Enter a Zip Code to fetch local weather data: "))
    jprint(weatherGetter(location))
    
