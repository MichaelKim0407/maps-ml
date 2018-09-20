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
    def __init__(self, x=None, y=None, lat=None, long=None, city=None):
        self.x = x
        self.y = y
        self.lat = lat
        self.long = long
        self.city = city

        self.__fill()

    def __fill(self):
        if self.x is not None:
            if self.lat is None:
                self.lat = to_lat(self.x)
        elif self.lat is not None:
            self.x = to_x(self.lat)
        else:
            raise ValueError('Provide x or lat')

        if self.y is not None:
            if self.long is None:
                self.long = to_long(self.y)
        elif self.long is not None:
            self.y = to_y(self.long)
        else:
            raise ValueError('Provide y or long')

        if self.city is None:
            self.city = api.get_city(self.lat, self.long)

    def __str__(self):
        return "{self.x},{self.y},{self.lat},{self.long},{self.city}".format(self=self)


def read_line(line):
    x, y, lat, long, city = line.split(",")
    return Location(
        float(x),
        float(y),
        float(lat),
        float(long),
        city
    )


def read_files(*files):
    for file in files:
        with open(file) as f:
            for line in f:
                line = line.strip()
                yield read_line(line)
