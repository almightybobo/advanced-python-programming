class Weight(object):
    def __init__(self, kilograms=None, pounds=None):
        if not any([kilograms, pounds]):
            raise ValueError('Provide at least one weight value')

        self._kilograms = kilograms
        self._pounds = pounds

    @property
    def kilograms(self):
        return self._kilograms or self._pounds / 2.2

    @property
    def pounds(self):
        return self._pounds or self._kilograms * 2.2

    def __add__(self, other):
        if self._kilograms:
            return Weight(
                kilograms=(self.kilograms + other.kilograms))
        return Weight(pounds=(self.pounds + other.pounds))
