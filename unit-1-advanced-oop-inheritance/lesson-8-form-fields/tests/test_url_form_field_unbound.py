import pytest

def test_url_form_field_unbound():
    twitter_field = URLField("Twitter profile URL?")

    with pytest.raises(ValueError):
        twitter_field.is_valid()
