# I used the OpenWeatherMap API to retrieve weather data and use the requests library in Python to fetch the weather API.

from urllib import response
import requests

API_KEY = "b5040be2ea75d836a9a9f5491c55479b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name here: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperture = round(data["main"]["temp"] - 273.15)
    print(f"Weather conditions in {city}: ", weather)
    print(f"Temperature in {city}: ", temperture, "celsius")
else:
    print("An error occured")
