import geopy.distance


class Coordinates:

    def __init__(self, lon: float, lan: float):
        self.lon = lon
        self.lan = lan

    def get(self):
        return self.lon, self.lan

    def is_close(self, other: "Coordinates", distance: float):
        return self.distance(other) < distance

    def distance(self, other: "Coordinates"):
        return geopy.distance.geodesic((self.lon, self.lan), (other.lon, other.lan)).m
