class FormField(object):
    def __init__(self, title, help_text=None):
        pass

    def submit_answer(self, answer):
        pass

    def get_answer(self):
        pass

    def is_valid(self):
        raise NotImplementedError()


class TextField(FormField):
    pass


class EmailField(FormField):
    pass


class URLField(FormField):
    pass


class MultipleChoiceField(FormField):
    def __init__(self, title, options, help_text=None):
        pass
