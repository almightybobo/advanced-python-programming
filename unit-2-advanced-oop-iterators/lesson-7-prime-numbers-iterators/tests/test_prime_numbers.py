def test_prime_numbers():
    iterator = iter(PrimeNumbersIterator())

    assert next(iterator) == 2
    assert next(iterator) == 3
    assert next(iterator) == 5
    assert next(iterator) == 7
    assert next(iterator) == 11
    assert next(iterator) == 13
    assert next(iterator) == 17
    assert next(iterator) == 19
    assert next(iterator) == 23
    assert next(iterator) == 29
    assert next(iterator) == 31
    assert next(iterator) == 37
