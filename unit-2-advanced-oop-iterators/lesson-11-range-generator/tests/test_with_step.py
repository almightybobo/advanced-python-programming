import pytest

def test_with_step():
    gen1 = iter(rmotr_range(2, 10, 2))
    assert next(gen1) == 2
    assert next(gen1) == 4
    assert next(gen1) == 6
    assert next(gen1) == 8
    with pytest.raises(StopIteration):
        next(gen1)
