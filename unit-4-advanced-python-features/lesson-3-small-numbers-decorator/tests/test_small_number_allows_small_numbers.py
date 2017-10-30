def test_small_number_allows_small_numbers():
    @small_numbers
    def a_testing_function(a, b, c):
        return "All good!"

    assert a_testing_function(3, 99, "Good?") == "All good!"
