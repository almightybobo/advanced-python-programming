class CountUpToIterator(object):
    def __init__(self, up_to):
        self.current = 0
        self.up_to = up_to

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.up_to:
            raise StopIteration()

        number = self.current
        self.current += 1
        return number

    next = __next__
