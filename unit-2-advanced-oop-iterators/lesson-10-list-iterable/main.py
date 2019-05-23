class ListIterable(object):
    def __init__(self, number_list):
        self.number_list = number_list
        self.index = 0

    def __next__(self):
        index = self.index
        self.index += 1
        if self.index > len(self.number_list):
            raise StopIteration

        return self.number_list[index]

    next = __next__


class ListIterator(object):
    def __init__(self, number_list):
        self.number_list = number_list

    def __iter__(self):
        return ListIterable(self.number_list)


if __name__ == '__main__':
    iterator = ListIterator([3, 2, 1])
    for elem in iterator:
        print(elem)
    print("====================")
    for elem in iterator:
        print(elem)
