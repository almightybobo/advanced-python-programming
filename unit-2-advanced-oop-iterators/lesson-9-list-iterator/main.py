class ListIterator(object):
    def __init__(self, number_list):
        self.number_list = number_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 1
        if self.index > len(self.number_list):
            exit()
            # better answer ( below )
            # raise StopIteration

        return self.number_list[index]

    next = __next__

if __name__ == '__main__':
    for elem in ListIterator([3, 2, 1]):
        print(elem)
