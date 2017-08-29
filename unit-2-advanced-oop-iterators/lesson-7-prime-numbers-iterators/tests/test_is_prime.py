def test_is_prime():
    obj = PrimeNumbersIterator()
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for number in prime_numbers:
        assert obj._is_prime(number) is True, "{} should be prime".format(number)

    not_prime_numbers = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 24, 25, 26]

    for number in not_prime_numbers:
        assert obj._is_prime(number) is False, "{} should NOT be prime".format(number)
