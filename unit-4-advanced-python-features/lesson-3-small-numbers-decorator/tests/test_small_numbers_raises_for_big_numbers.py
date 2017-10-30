import pytest


def test_small_numbers_raises_for_big_numbers():
    @small_numbers
    def a_testing_function(a, b, c):
        return "You Should never see this!"

    with pytest.raises(ValueError):
        assert a_testing_function(3, 102, "Good?")
