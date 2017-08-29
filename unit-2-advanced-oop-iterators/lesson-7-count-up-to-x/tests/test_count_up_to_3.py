import pytest

def test_count_up_to_3():
    iterator = iter(CountUpToIterator(up_to=3))

    assert next(iterator) == 0
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3

    with pytest.raises(StopIteration):
        next(iterator)
