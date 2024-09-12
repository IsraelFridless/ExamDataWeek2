from typing import List
import json

from api.geo_api import get_city_coordinates
from models.aircraft import Aircraft
from models.pilot import Pilot
from models.target import Target
from models.weather import Weather


def read_pilots_from_json(filename: str) -> List[Pilot]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Pilot(pilot['name'], pilot['skill']) for pilot in data]

def read_airplanes_from_json(filename: str) -> List[Aircraft]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Aircraft(aircraft['type'], aircraft['speed'], aircraft['fuel_capacity']) for aircraft in data]

def read_targets_from_json(filename: str) -> List[Target]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Target(target['city'], target['priority'], get_city_coordinates()) for target in data]

def read_weather_from_json(filename: str) -> List[Weather]:
    with open(filename, 'r') as jsonfile:
        data = json.load(jsonfile)
    return [Weather(weather['weather']['main'], weather['clouds']['all'], weather['wind']['speed']) for weather in data]