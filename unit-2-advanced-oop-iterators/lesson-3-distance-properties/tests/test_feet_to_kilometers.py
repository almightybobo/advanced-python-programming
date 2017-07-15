import pytest


def test_feet_to_kilometers():
    d = Distance(feet=25000)

    assert d.distance_in_feet == 25000
    assert d.distance_in_kilometers == pytest.approx(7.62, rel=1e-2)
