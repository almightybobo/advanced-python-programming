def test_email_field_is_valid():
    email_field = EmailField("What's your email?")
    email_field.submit_answer('questions@rmotr.com')
    assert email_field.is_valid()
