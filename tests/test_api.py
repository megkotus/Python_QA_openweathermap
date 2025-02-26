import pytest

from data.urls import Urls
from utils.api_functions import get_weather_by_city_name, get_weather_by_zip_code, get_weather_by_city_id, \
    get_cities_id_by_city_name

urls = Urls()

@pytest.mark.parametrize('city', ['London', 'Podgorica', 'Berlin', 'Dubrovnik'])
def test_weather_api_returns_correct_city_name(city):
    response = get_weather_by_city_name(city)
    json_data = response.json()
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert json_data['name'] == city, f"Expected {city}, but got {json_data['name']}"

def test_get_weather_by_city_name_without_api_key():
    response = get_weather_by_city_name('Budva', app_id = None)
    assert response.status_code == 401, f'Expected 401, got {response.status_code}'

def test_get_weather_by_zip_code_without_api_key():
    response = get_weather_by_zip_code('191028', app_id = None)
    assert response.status_code == 401, f'Expected 401, got {response.status_code}'

@pytest.mark.parametrize('city', ['London', 'Podgorica', 'Berlin', 'Dubrovnik'])
def test_weather_api_returns_correct_city_by_id(city):
    response_city_id = get_cities_id_by_city_name(city)
    response = get_weather_by_city_id(response_city_id[city])
    assert response.status_code == 200, f'Expected 200, got {response.status_code}'
    assert response.json()['name'] == city, f'Expected {city}, got {response.json()["name"]}'