def test_subtract_function():

    @pretty_result
    def subtract(x, y):
        return x - y

    assert subtract(13, 8) == "The result of the function 'subtract' is: 5"
