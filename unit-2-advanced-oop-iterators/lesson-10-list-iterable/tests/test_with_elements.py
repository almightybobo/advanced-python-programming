import pytest

def test_with_elements():
    iterator = ListIterator(['a', 'b', 'c'])
    it = iter(iterator)

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

    with pytest.raises(StopIteration):
        next(it)

    it = iter(iterator)

    assert next(it) == 'a'
    assert next(it) == 'b'
    assert next(it) == 'c'

    with pytest.raises(StopIteration):
        next(it)
