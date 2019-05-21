# Hint: don't forget the custom exception
class OperationException(Exception):
    pass


class Operation(object):
    def __init__(self, *args):
        self.args = args

    def operate(self):
        raise NotImplementedError()


class AddOperation(Operation):
    # The only method present in this class
    def operate(self):
        return sum(self.args)

class SubtractOperation(Operation):
    def operate(self):
        result = self.args[0]
        for arg in self.args[1:]:
            result -= arg
        return result
    # other method
    # def operate(self):
    #     if not self.args:
    #         return 0
    #     return self.args[0] - sum(self.args[1:])


class Calculator(object):
    def __init__(self, operations):
        self.operations = operations

    def calculate(self, *args):
        numbers, operation = args[:-1], args[-1]
        if operation not in self.operations:
            raise OperationException
        operation = self.operations[operation](*numbers)
        return operation.operate()


if __name__ == '__main__':
    calc1 = Calculator(operations={
            'add': AddOperation,
            'subtract': SubtractOperation})

    calc2 = Calculator(operations={
            'add': AddOperation})

    print(calc1.calculate(2, 1, 5, 'add'))  # Should return 2 + 1 + 5 = 8
    print(calc2.calculate(1, 5, 'add'))  # Should return 1 + 5 = 6

    op = AddOperation(2, 1, 5)
    print(op.operate())  # Should return 8
