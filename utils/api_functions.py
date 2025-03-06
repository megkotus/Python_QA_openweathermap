import os
import requests

from data.urls import Urls

urls = Urls()

if not os.getenv('CI'):
    from dotenv import load_dotenv

    load_dotenv()

api_key = os.getenv('SECRET_KEY')


def get_weather_by_city_name(city, app_id=api_key):
    response = requests.get(urls.api_url, params={'q': city, 'appid': app_id})
    return response


def get_weather_by_zip_code(zip_code, app_id=api_key):
    response = requests.get(
        urls.api_url, params={'q': zip_code, 'appid': app_id}
    )
    return response


def get_weather_by_city_id(city_id, app_id=api_key):
    response = requests.get(
        urls.api_url, params={'id': city_id, 'appid': app_id}
    )
    return response


def get_cities_id_by_city_name(city):
    response = get_weather_by_city_name(city)
    data = response.json()
    return {city: data['id']}
