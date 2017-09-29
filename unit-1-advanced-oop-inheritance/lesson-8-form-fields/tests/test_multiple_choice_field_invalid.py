def test_multiple_choice_field_invalid():
    multi_field = MultipleChoiceField(
        "What's your preferred language?",
        ['Python', 'Ruby', 'Javascript'])

    multi_field.submit_answer('Invalid Language')
    assert not multi_field.is_valid()
