import pytest

def test_with_empty_list():
    it = iter(ListIterator([]))
    with pytest.raises(StopIteration):
        next(it)
