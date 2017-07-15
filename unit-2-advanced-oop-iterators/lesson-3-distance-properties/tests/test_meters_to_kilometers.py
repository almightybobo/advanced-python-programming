def test_meters_to_kilometers():
    d = Distance(meters=8000)

    assert d.distance_in_meters == 8000
    assert d.distance_in_kilometers == 8
