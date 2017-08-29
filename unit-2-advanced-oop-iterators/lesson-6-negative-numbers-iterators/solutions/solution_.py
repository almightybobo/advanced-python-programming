class NegativeNumbersIterator(object):
    def __init__(self):
        self.next_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        number = self.next_number
        self.next_number -= 1
        return number

    next = __next__
