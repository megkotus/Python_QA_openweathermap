import pytest
import os
import requests

from data.urls import Urls

if not os.getenv('CI'):
    from dotenv import load_dotenv
    load_dotenv()

api_key = os.getenv('SECRET_KEY')
urls = Urls()

@pytest.mark.parametrize('city', ['London', 'Podgorica', 'Berlin', 'Dubrovnik'])
def test_weather_api_returns_correct_city_name(city):
    response = requests.get(urls.api_url, params={'q': city, 'appid': api_key})
    json_data = response.json()
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert json_data['name'] == city, f"Expected {city}, but got {json_data['name']}"

def test_api_key_is_required():
    response = requests.get(urls.api_url, params={'q': 'Budva'})
    assert response.status_code == 401