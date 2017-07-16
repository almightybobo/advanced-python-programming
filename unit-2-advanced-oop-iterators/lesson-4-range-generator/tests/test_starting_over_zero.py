import pytest

def test_starting_over_zero():
    gen1 = iter(rmotr_range(3, 6))
    assert next(gen1) == 3
    assert next(gen1) == 4
    assert next(gen1) == 5
    with pytest.raises(StopIteration):
        next(gen1)
