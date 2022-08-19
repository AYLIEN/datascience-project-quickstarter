from aylien_model_serving.app_factory import FlaskAppWrapper
from {{PKG_NAME}}.example_module import Counter, TextReverser


def run_app():
    """
    This is a mock app, showing how to make simple requests.
    """
    counter = Counter()
    text_reverser = TextReverser()

    def reverse_text(text):
        nonlocal text_reverser
        text = "".join(list(reversed(text)))
        response = {"text": text}
        return response

    def increment_count():
        nonlocal counter
        count = counter()
        response = {"count": count}
        return response

    def process_reverse_text():
        return FlaskAppWrapper.process_json(reverse_text)

    def process_increment_count():
        return FlaskAppWrapper.process_json(increment_count)

    routes = [
        {
            "endpoint": "/reverse",
            "callable": process_reverse_text,
            "methods": ["POST"]
        },
        {
            "endpoint": "/count",
            "callable": process_increment_count,
            "methods": ["POST"]
        },
    ]

    return FlaskAppWrapper.create_app(routes)
