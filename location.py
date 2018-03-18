import api

__author__ = 'Michael'

MIN_LAT = 33.76
MIN_LONG = -117.95
MAX_LAT = 33.63
MAX_LONG = -117.68
LAT_RANGE = MAX_LAT - MIN_LAT
LONG_RANGE = MAX_LONG - MIN_LONG


def to_lat(x):
    return MIN_LAT + LAT_RANGE * x


def to_long(y):
    return MIN_LONG + LONG_RANGE * y


def to_x(lat):
    return (lat - MIN_LAT) / LAT_RANGE


def to_y(long):
    return (long - MIN_LONG) / LONG_RANGE


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lat = to_lat(x)
        self.long = to_long(y)
        self.city = api.get_city(self.lat, self.long)

    def __str__(self):
        return f"{self.x},{self.y},{self.lat},{self.long},{self.city}"
