import pytest

def test_add_kilograms_to_pounds():
    w1 = Weight(kilograms=80)
    w2 = Weight(pounds=46)
    w3 = w1 + w2

    assert w3.kilograms == pytest.approx(100.90, rel=1e-2)
    assert w3.pounds == pytest.approx(222.0)
