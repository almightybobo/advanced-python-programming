class PrimeNumbersIterator(object):
    def __init__(self):
        self.next_number = 2

    def __iter__(self):
        return self

    def _is_prime(self, number):
        if number in (2, 3):
            return True

        if number % 2 == 0:
            return False

        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def __next__(self):
        number = self.next_number
        while not self._is_prime(number):
            number += 1

        self.next_number = number + 1
        return number

    next = __next__
