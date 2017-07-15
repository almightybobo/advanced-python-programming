def test_respects_passed_length():
    length_2 = SimplePasswordGenerator(length=2)
    length_2_it = iter(length_2)
    assert len(next(length_2_it)) == 2

    length_4 = SimplePasswordGenerator(length=4)
    length_4_it = iter(length_4)
    assert len(next(length_4_it)) == 4

    length_16 = SimplePasswordGenerator(length=16)
    length_16_it = iter(length_16)
    assert len(next(length_16_it)) == 16
