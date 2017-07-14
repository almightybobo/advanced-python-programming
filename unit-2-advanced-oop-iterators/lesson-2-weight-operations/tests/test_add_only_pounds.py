def test_add_only_pounds():
    w1 = Weight(pounds=37)
    w2 = Weight(pounds=22)
    w3 = w1 + w2

    assert w3.pounds == 59
