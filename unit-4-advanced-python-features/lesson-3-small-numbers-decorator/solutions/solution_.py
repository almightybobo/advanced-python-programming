def small_numbers(fn):
    def wrapped(*args, **kwargs):
        for arg in args:
            if type(arg) in [int, float]:
                if arg > 100:
                    raise ValueError("Only small numbers allowed!")

        return fn(*args, **kwargs)
    return wrapped
