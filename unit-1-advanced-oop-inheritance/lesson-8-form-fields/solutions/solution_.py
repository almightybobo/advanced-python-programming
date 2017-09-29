class FormField(object):
    def __init__(self, title, help_text=None):
        self.title = title
        self.help_text = help_text
        self.answer = None

    def submit_answer(self, answer):
        self.answer = answer

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
        return (
            self.answer.startswith('https://') or
            self.answer.startswith('http://')
        )


class MultipleChoiceField(FormField):
    def __init__(self, title, options, help_text=None):
        super(MultipleChoiceField, self).__init__(title, help_text)
        self.options = options

    def is_valid(self):
        super(MultipleChoiceField, self).is_valid()
        return self.answer in self.options
