def test_meters_to_feet():
    d = Distance(meters=8000)

    assert d.distance_in_meters == 8000
    assert d.distance_in_feet == 26240
