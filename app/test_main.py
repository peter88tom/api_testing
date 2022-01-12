import requests
from .main import app

# Require parameters
country_code = "za"
zip_code = 2192


def test_get_location(country_code, zip_code):
  response = requests.get(f"http://api.zippopotam.us/{country_code}/{zip_code}")
  assert response.status_code == 200
