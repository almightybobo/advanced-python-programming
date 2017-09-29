# Form Fields

In this assignment you'll implement the models (high level classes) to create a clone of Google Forms. You're in charge of implementing the Form fields. Most form fields are similar (they have a title and a help text and accept an answer), so we don't want to duplicate a lot of logic.

You should rely primarily on the tests to make this assignment work.

**Form creation and submitting answers**

A form field is going to be created by passing a title and optionally a help text. `MultipleChoiceField`s will also accept `options`. Once you have created your field you can invoke the `submit_answer()` method. And after an answer was recorded, you can invoke the `is_valid()` method that will return if the answer was valid.

If you try to invoke `is_valid` in a form field that hasn't recorded an answer yet (an "unbound" field) that'll result in a `ValueError` exception raised. Examples:

```python
text_field = TextField(
      "What do you like about RMOTR?",
      help_text="Mentors? Classes? Assignments?")
print(text_field.help_text)  # "Mentors? Classes? Assignments?"

text_field.is_valid()  # WARNING! Raises ValueError

text_field.submit_answer('Mentoring!')

text_field.is_valid()  # True
```
