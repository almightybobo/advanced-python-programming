class Calculator(object):
    def __init__(self):
        pass

    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def subtract(clss, x, y):
        return clss.add(x, y * -1)

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        return x / y

if __name__ == '__main__':
    print(Calculator.add(2, 4))  # 6
    print(Calculator.subtract(8, 1))  # 7
    print(Calculator.multiply(3, 5))  # 15
    print(Calculator.divide(5, 2))  # 2.5
