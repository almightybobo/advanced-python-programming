import random
import string

class SimplePasswordGenerator(object):
    def __init__(self, available_chars=None, length=8):
        if not available_chars:
            available_chars = list(string.digits + string.ascii_letters + string.punctuation)
        self.available_chars = available_chars
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        result = []
        for i in range(self.length):
            result.append(random.choice(self.available_chars))

        return ''.join(result)

if __name__ == '__main__':
    pass_generator = SimplePasswordGenerator()
    print(next(pass_generator))
    print(next(pass_generator))

    pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
    print(next(pass_generator))
