"""
I’ll be using the Zippopotam.us REST API. 
This API takes a country code and a zip code and returns 
location data associated with that country and zip code.
For example, a GET request to http://api.zippopotam.us/us/90210
"""

from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def get_location(country_code: str, zip_code: int):
	response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
	response = response.json()
	return {"data": response}