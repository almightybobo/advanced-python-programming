def test_url_field_is_valid():
    twitter_field = URLField("Twitter profile URL?")
    twitter_field.submit_answer('https://twitter.com/rmotr_com')
    assert twitter_field.is_valid()
