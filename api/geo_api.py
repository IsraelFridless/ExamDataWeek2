from logging import exception
from typing import Tuple, List, Dict

import requests

API_KEY = "5061bcf4f469b3b4dc16dfbe7a8e3f6f"

def get_city_coordinates(city: str) -> Tuple[(float, float)]:
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={API_KEY}"
    try:
        res = requests.get(url)
        if res.status_code != 200:
            raise Exception("something went wrong")
        data = res.json()
        info = data[0]
        lat: float = info.get('lat')
        lon: float = info.get('lon')
        return (lat, lon)
    except exception as ex:
        raise Exception(ex)

def get_coordinates_for_cities(cities: List[str]) -> Dict[str, (float, float)]:
    return {city: get_city_coordinates(city) for city in cities}
