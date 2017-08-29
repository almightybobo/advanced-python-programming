def test_negative_numbers():
    iterator = iter(NegativeNumbersIterator())

    assert next(iterator) == 0
    assert next(iterator) == -1
    assert next(iterator) == -2
    assert next(iterator) == -3
