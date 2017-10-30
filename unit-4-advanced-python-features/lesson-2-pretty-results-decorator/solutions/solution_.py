def pretty_result(original_function):
    def wrapped(a, b):
        original_result = original_function(a, b)
        function_name = original_function.__name__
        return "The result of the function '{}' is: {}".format(
            function_name, original_result)
    return wrapped
