class PrimeNumbersIterator(object):
    def __iter__(self):
        self.next_number = 2
        return self

    def _is_prime(self, number):
        if number <= 1:
            return False
        else:
            for i in range(2, number):
                if number % i == 0:
                    return False
            return True

    def __next__(self):
        while(1):
            number = self.next_number
            if self._is_prime(number):
                self.next_number += 1
                return number
            else:
                self.next_number += 1

        # other solution
        '''
        number = self.next_number
        while not self._is_prime(number):
            number += 1

        self.next_number = number + 1
        return number
        '''

    next = __next__


if __name__ == '__main__':
    obj = PrimeNumbersIterator()
    print(obj._is_prime(3))  # True
    print(obj._is_prime(199))  # True
    print(obj._is_prime(20))  # False

    iterator = iter(PrimeNumbersIterator())

    print(next(iterator))  # 2
    print(next(iterator))  # 3
    print(next(iterator))  # 5
    print(next(iterator))  # 7
    print(next(iterator))  # 11
