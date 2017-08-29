class ListIterable(object):
    def __next__(self):
        pass


class ListIterator(object):
    def __iter__(self):
        pass

# iterator = ListIterator([3, 2, 1])
# for elem in iterator:
#     print(elem)
# print("====================")
# for elem in iterator:
#     print(elem)
