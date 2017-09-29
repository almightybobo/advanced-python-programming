def test_url_field_is_invalid():
    twitter_field = URLField("Twitter profile URL?")
    twitter_field.submit_answer('INVALID URL')

    assert not twitter_field.is_valid()
