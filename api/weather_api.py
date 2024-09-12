from logging import exception
from typing import Tuple, List, Dict

import requests

from api.geo_api import API_KEY
from models.weather import Weather


def get_weather_by_city_name(city: str) -> Weather:
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    try:
        res = requests.get(url)
        if res.status_code != 200:
            raise Exception("something went wrong")
        data = res.json()
        filtered = next(map(lambda x: x['dt_txt'].endswith('00:00:00'), data))
        return filtered
    except exception as ex:
        raise Exception(ex)

def get_weather_for_cities(cities: List[str]) -> Dict[str, Weather]:
    return {city: get_weather_by_city_name(city) for city in cities}
