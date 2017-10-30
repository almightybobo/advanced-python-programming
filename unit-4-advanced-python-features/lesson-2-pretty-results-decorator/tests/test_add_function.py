def test_add_function():
    @pretty_result
    def add(x, y):
        return x + y

    assert add(2, 5) == "The result of the function 'add' is: 7"
