import pytest

def test_with_empty_list():
    iterator = ListIterator([])
    it = iter(iterator)
    with pytest.raises(StopIteration):
        next(it)

    it = iter(iterator)
    with pytest.raises(StopIteration):
        next(it)
