import pytest

def test_email_form_field_unbound():
    email_field = EmailField("What's your email?")

    with pytest.raises(ValueError):
        email_field.is_valid()
