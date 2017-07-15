def test_meters_to_miles():
    d = Distance(meters=8000)

    assert d.distance_in_meters == 8000
    assert d.distance_in_miles == 5
