class CountUpToIterator(object):
    def __init__(self, up_to):
        self.number = 0
        self.up_to = up_to

    def __iter__(self):
        return self

    def __next__(self):
        number = self.number
        self.number += 1
        if number > self.up_to:
            raise StopIteration()
        return number

    next = __next__

if __name__ == '__main__':
    iterator = iter(CountUpToIterator(up_to=5))
    print(next(iterator)) # 0
    print(next(iterator)) # 1
    print(next(iterator)) # 2
    print(next(iterator)) # 3
    print(next(iterator)) # 4
    print(next(iterator)) # 5
    print(next(iterator)) # StopIteration() Raised!
