import pytest

def test_count_up_to_1():
    iterator = iter(CountUpToIterator(up_to=1))

    assert next(iterator) == 0
    assert next(iterator) == 1

    with pytest.raises(StopIteration):
        next(iterator)
