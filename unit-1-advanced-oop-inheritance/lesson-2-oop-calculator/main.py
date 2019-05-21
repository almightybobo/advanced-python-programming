class Calculator(object):
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

if __name__ == '__main__':
    calculator = Calculator()

    print(calculator.add(2, 4))  # 6
    print(calculator.subtract(8, 1))  # 7
    print(calculator.multiply(3, 5))  # 15
    print(calculator.divide(5, 2))  # 2.5
