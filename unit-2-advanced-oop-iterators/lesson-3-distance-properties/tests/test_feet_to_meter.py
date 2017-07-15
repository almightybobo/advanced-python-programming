import pytest

def test_feet_to_meter():
    d = Distance(feet=25000)

    assert d.distance_in_feet == 25000
    assert d.distance_in_meters == pytest.approx(7621.95, rel=1e-2)
