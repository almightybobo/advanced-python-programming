import pytest

def test_url_form_field_unbound():
    twitter_field = URLField("Twitter profile URL?")

    with pytest.raises(ValueError):
        twitter_field.is_valid()


import pytest

def test_multiple_choice_form_field_unbound():
    multi_field = MultipleChoiceField(
        "What's your preferred language?",
        ['Python', 'Ruby', 'Javascript'],
        help_text="There's only one correct answer ;)")

    with pytest.raises(ValueError):
        multi_field.is_valid()

    assert multi_field.help_text == "There's only one correct answer ;)"
