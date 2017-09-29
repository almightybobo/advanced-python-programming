def test_text_form_fields():
    text_field = TextField(
        "What do you like about RMOTR?",
        help_text="Mentors? Classes? Assignments?")

    text_field.submit_answer('Mentoring, for sure!')

    assert text_field.is_valid()
