class Distance(object):
    def __init__(self, meters=None, feet=None):
        # Please don't change this method
        if not any((meters, feet)):
            raise ValueError("Provide at least one measure of distance")

        self.meters = meters
        self.feet = feet

    @property
    def distance_in_feet(self):
        return self.feet or self.meters * 3.281

    @property
    def distance_in_meters(self):
        return self.meters or self.feet / 3.281

    @property
    def distance_in_kilometers(self):
        return self.distance_in_meters / 1000

    @property
    def distance_in_miles(self):
        return self.distance_in_kilometers / 1.61


if __name__ == '__main__':
    d = Distance(meters=8000)
    print(d.distance_in_kilometers) ## 8
    print(d.distance_in_miles) ## 5

    d = Distance(feet=25000)
    print(d.distance_in_kilometers) ## 7.62
    print(d.distance_in_meters) ## 7621.95


