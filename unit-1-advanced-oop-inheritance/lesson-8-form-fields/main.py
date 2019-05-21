class FormField(object):
    def __init__(self, title, help_text=None):
        self.title = title
        self.help_text = help_text
        self.answer = None

    def submit_answer(self, answer):
        self.answer = answer

        return answer

    def get_answer(self):
        pass

    def is_valid(self):
        if not self.answer:
            raise ValueError()

        return True


class TextField(FormField):
    pass


class EmailField(FormField):
    def is_valid(self):
        super(EmailField, self).is_valid()
        return '@' in self.answer

class URLField(FormField):
    def is_valid(self):
        super(URLField, self).is_valid()
        return ('http://' in self.answer
            or 'https://' in self.answer)
        # better answer
        # return (self.answer.startswith('https://') or self.answer.startswith('http://'))


class MultipleChoiceField(FormField):
    def __init__(self, title, options, help_text=None):
        super(MultipleChoiceField, self).__init__(title, help_text)
        self.options = options

    def is_valid(self):
        super(MultipleChoiceField, self).is_valid()
        return self.answer in self.options


if __name__ == '__main__':
    text_field = TextField(
              "What do you like about RMOTR?",
              help_text="Mentors? Classes? Assignments?")
    print(text_field.help_text)  # "Mentors? Classes? Assignments?"

    # print(text_field.is_valid())  # WARNING! Raises ValueError

    text_field.submit_answer('Mentoring!')

    print(text_field.is_valid())  # True
