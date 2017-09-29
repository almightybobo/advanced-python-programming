def test_multiple_choice_field_is_valid():
    multi_field = MultipleChoiceField(
        "What's your preferred language?",
        ['Python', 'Ruby', 'Javascript'],
        help_text="There's only one correct answer ;)")

    multi_field.submit_answer('Python')
    assert multi_field.is_valid()

    assert multi_field.help_text == "There's only one correct answer ;)"
