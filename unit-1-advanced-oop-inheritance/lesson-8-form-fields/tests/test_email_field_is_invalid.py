def test_email_field_is_invalid():
    email_field = EmailField("What's your email?")
    email_field.submit_answer('INVALID EMAIL')
    assert not email_field.is_valid()
