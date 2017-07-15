import pytest

def test_feet_to_miles():
    d = Distance(feet=25000)

    assert d.distance_in_feet == 25000
    assert d.distance_in_miles == pytest.approx(4.76, rel=1e-2)
