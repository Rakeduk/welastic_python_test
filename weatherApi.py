import requests
import api_key
import json

towns = ["Warsaw", "London", "New York"]

for town in towns:
	response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key.weather_key}&q={town}&aqi=no")
	weather = response.json()['current']['temp_c']
	print(town, weather)