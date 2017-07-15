class Distance(object):
    def __init__(self, meters=None, feet=None):
        # Please don't change this method
        if not any((meters, feet)):
            raise ValueError("Provide at least one measure of distance")

        self.meters = meters
        self.feet = feet
