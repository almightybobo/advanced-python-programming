import pytest

def test_with_elements():
    it = iter(ListIterator(['a', 'b', 'c']))

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

    with pytest.raises(StopIteration):
        next(it)
