class Weight(object):
    def __init__(self, kilograms=None, pounds=None):
        if not any([kilograms, pounds]):
            raise ValueError('Provide at least one weight value')

        self._kg = kilograms
        self._lb = pounds

    @property
    def kilograms(self):
        if self._kg is not None:
            return self._kg
        return self._lb * 0.453592

    @property
    def pounds(self):
        if self._lb is not None:
            return self._lb
        return self._kg * 2.20462

    def __add__(self, other):
        if self._kg is not None:
            return Weight(kilograms=(self.kilograms + other.kilograms))
        return Weight(pounds=(self.pounds + other.pounds))
