class TextReverser:
    """
    Dummy class that performs a toy task (reversing texts).
    """
    def __call__(self, text):
        new_text = "".join(list(reversed(text)))
        return new_text


class Counter:
    """
    Dummy class that performs a toy task (counting).
    """
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count
