import pytest

def test_text_form_field_unbound():
    text_field = TextField(
        "What do you like about RMOTR?",
        help_text="Mentors? Classes? Assignments?")

    with pytest.raises(ValueError):
        text_field.is_valid()

    assert text_field.help_text == "Mentors? Classes? Assignments?"
