import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://api.open-meteo.com/v1/forecast"

#Cracow crodinates
params = {
    "latitude": 50.0614, 
    "longitude": 19.9366, 
    "current": "temperature_2m", 
    "timezone": "Europe/Warsaw"
}

#Get data
responses = openmeteo.weather_api(url, params=params)
response = responses[0] #First

#Current data
current = response.Current()

temp_now = current.Variables(0).Value()

#Temperature output
print(temp_now)
