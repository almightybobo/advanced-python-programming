def test_add_only_kilograms():
    w1 = Weight(kilograms=80)
    w2 = Weight(kilograms=25)
    w3 = w1 + w2

    assert w3.kilograms == 105
