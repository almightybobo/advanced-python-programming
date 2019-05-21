# 1 pound = 0.4536 kg

class Weight(object):
    def __init__(self, kilograms=None, pounds=None):
        if not any([kilograms, pounds]):
            raise ValueError()
        self._kilograms = kilograms
        self._pounds = pounds

    @property
    def kilograms(self):
        return self._kilograms or self._pounds * 0.4536

    @property
    def pounds(self):
        return self._pounds or self._kilograms / 0.4536

    def __add__(self, other):
        if self._kilograms:
            return Weight(kilograms=(self.kilograms + other.kilograms))
        return Weight(pounds=(self.pounds + other.pounds))


if __name__ == '__main__':
    w1 = Weight(kilograms=80)
    w2 = Weight(pounds=46)
    w3 = w1 + w2

    print(w3.kilograms)  # 100.90
    print(w3.pounds)  # 222.0
