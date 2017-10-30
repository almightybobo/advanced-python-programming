import pytest

def test_with_only_one_parameter():
    @small_numbers
    def a_testing_function(a):
        return "You see me?"

    # Works with a small param
    assert a_testing_function(3) == "You see me?"

    # But fails with a large one:
    with pytest.raises(ValueError):
        assert a_testing_function(105)
