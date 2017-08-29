class NumbersIterator(object):
    def __init__(self):
        self.next_number = 1

    def __iter__(self):
        return self

    def __next__(self):
        pass

    next = __next__


# iterator = iter(NumbersIterator())
#
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
