def test_uses_available_chars():
    pass_gen = SimplePasswordGenerator(available_chars=['a', 'b'], length=2)
    it = iter(pass_gen)
    password = next(it)

    assert (
        set(password) == set(['a', 'b']) or
        set(password) == set(['a']) or
        set(password) == set(['b'])
    )
