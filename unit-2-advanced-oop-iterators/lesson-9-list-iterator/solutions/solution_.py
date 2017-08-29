class ListIterator(object):
    def __init__(self, elems):
        self.elems = elems
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.elems):
            raise StopIteration()

        elem = self.elems[self.index]
        self.index += 1

        return elem

    next = __next__
