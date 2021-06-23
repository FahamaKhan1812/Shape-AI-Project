import requests
import os
from datetime import datetime

file = open('weather_report.txt', 'a')

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


file.write("-------------------------------------------------------------\n")
file.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
file.write("-------------------------------------------------------------\n")

file.write("Current temperature is: {:.2f} deg C.\n".format(temp_city))
file.write("Current weather desc:\t{}.\n".format(weather_desc))
file.write("Current Humidity:\t\t{}%.\n".format(hmdt))
file.write("Current wind speed:\t\t{} KMPH\n\n".format(wind_spd))
file.close()





