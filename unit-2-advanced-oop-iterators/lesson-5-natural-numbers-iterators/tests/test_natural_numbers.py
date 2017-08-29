def test_natural_numbers():
    iterator = iter(NumbersIterator())

    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 4
