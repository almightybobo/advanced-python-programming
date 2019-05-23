def range_generator(start, end, step=1):
    result = start
    while result < end:
        num = result
        result += step
        yield num

class RangeIterator(object):
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.result = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.result < self.end:
            num = self.result
            self.result += self.step
            return num
        else:
            raise StopIteration

    next = __next__


if __name__ == '__main__':
    print('answer1')
    for num in range_generator(start=1, end=5):
        print(num)

    print('answer2')
    for num in range_generator(start=0, end=6, step=2):
        print(num)

    print('answer3')
    for num in RangeIterator(start=1, end=5):
        print(num)

    print('answer4')
    for num in RangeIterator(start=0, end=6, step=2):
        print(num)
