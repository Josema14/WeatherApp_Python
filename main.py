import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

API_Key = os.getenv('API_KEY')  # calling the environment variable
city = input("Enter a city: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={city}"

print(base_url)

weather_data = requests.get(base_url).json()

pprint(weather_data)
