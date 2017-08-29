import pytest

def test_starting_from_zero():
    gen1 = iter(rmotr_range(0, 3))
    assert next(gen1) == 0
    assert next(gen1) == 1
    assert next(gen1) == 2
    with pytest.raises(StopIteration):
        next(gen1)
