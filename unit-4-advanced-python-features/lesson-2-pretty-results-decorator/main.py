def pretty_result(func):
    def wrapper(a, b):
        result = str(func(a, b))
        return 'The result of the function {} is: {}'.format(func.__name__, result)
    return wrapper

@pretty_result
def add(x, y):
    return x + y

print(add(2, 5))
