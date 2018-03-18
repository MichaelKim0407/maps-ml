import googlemaps
import os

__author__ = 'Michael'

with open(os.path.join(os.path.dirname(__file__), 'key.txt')) as f:
    API_KEY = f.read().strip()
api = googlemaps.Client(key=API_KEY)


def get_location(address):
    results = api.geocode(address)
    result = results[0]
    location = result['geometry']['location']
    return location['lat'], location['lng']


def get_full_address(lat, long):
    results = api.reverse_geocode((lat, long))
    result = results[0]
    return result['formatted_address']


def get_address_component(lat, long, type):
    results = api.reverse_geocode((lat, long))
    for result in results:
        components = result['address_components']
        for component in components:
            if type in component['types']:
                return component
    return None


def get_city(lat, long):
    component = get_address_component(lat, long, 'locality')
    return component['long_name']
