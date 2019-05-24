def small_numbers(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) in [int, float]:
                if arg >= 100:
                    raise ValueError("Error")
        return fn(*args, **kwargs)
    return wrapper


@small_numbers
def my_func(number_param, string_param):
      pass

my_func(99, "Hello")
my_func(101, "Oh no!")
