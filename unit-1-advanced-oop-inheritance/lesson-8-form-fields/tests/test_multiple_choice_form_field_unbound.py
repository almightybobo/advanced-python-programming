import pytest

def test_multiple_choice_form_field_unbound():
    multi_field = MultipleChoiceField(
        "What's your preferred language?",
        ['Python', 'Ruby', 'Javascript'],
        help_text="There's only one correct answer ;)")

    with pytest.raises(ValueError):
        multi_field.is_valid()

    assert multi_field.help_text == "There's only one correct answer ;)"
