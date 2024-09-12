import math

import requests
from toolz import curry

from models.aircraft import Aircraft
from models.target import Target
from models.weather import Weather

# Function to calculate the distance between two coordinates using the Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
     r = 6371.0 # Radius of the Earth in kilometers
     # Convert degrees to radians
     lat1_rad = math.radians(lat1)
     lon1_rad = math.radians(lon1)
     lat2_rad = math.radians(lat2)
     lon2_rad = math.radians(lon2)
     # Calculate differences between the coordinates
     dlat = lat2_rad - lat1_rad
     dlon = lon2_rad - lon1_rad
     # Apply Haversine formula
     a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
     c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
     # Calculate the distance
     distance = r * c
     return distance

weights = {
    'distance': 0.20,
    'aircraft_type': 0.25,
    'pilot_skill': 0.25,
    'weather_conditions': 0.20,
    'execution_time': 0.10
}


cities = ['Damascus', 'Beirut', 'Amman', 'Cairo', 'Baghdad', 'Tehran', 'Riyadh', 'Tripoli', 'Ankara', 'Khartoum', 'Gaza City', 'Sanaa', 'Manama', 'Kuwait City', 'Doha']

def calculate_score(distance, aircraft_score, pilot_skill, weather_score, execution_time_score):
    return (distance * weights['distance'] +
            aircraft_score * weights['aircraft_type'] +
            pilot_skill * weights['pilot_skill'] +
            weather_score * weights['weather_conditions'] +
            execution_time_score * weights['execution_time'])

def aircraft_score(aircraft: Aircraft):
    # rating by abilities
    if aircraft == 'Stealth Fighter':
        return 1.0
    elif aircraft == 'Fighter Jet':
        return 0.9
    elif aircraft == 'Heavy Bomber':
        return 0.8
    elif aircraft == 'Bomber':
        return 0.7
    elif aircraft == 'Drone':
        return 0.6
    elif aircraft == 'Recon Drone':
        return 0.5
    elif aircraft == 'Helicopter':
        return 0.4
    else:
        return 0

def calculate_distance(target: Target) -> float:
    return haversine_distance(target.lat, target.lon, 32.081669, 34.841011)
