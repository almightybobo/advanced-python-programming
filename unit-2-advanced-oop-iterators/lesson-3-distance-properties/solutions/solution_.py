class Distance(object):
    def __init__(self, meters=None, feet=None):
        if not any((meters, feet)):
            raise ValueError("Provide at least one measure of distance")

        self.meters = meters
        self.feet = feet

    @property
    def distance_in_meters(self):
        return self.meters or self.feet / 3.28

    @property
    def distance_in_feet(self):
        return self.feet or self.meters * 3.28

    @property
    def distance_in_kilometers(self):
        return self.distance_in_meters / 1000.0

    @property
    def distance_in_miles(self):
        return self.distance_in_kilometers / 1.6


d = Distance(meters=8000)
assert d.distance_in_kilometers == 8, d.distance_in_miles
assert d.distance_in_miles == 5, d.distance_in_miles
