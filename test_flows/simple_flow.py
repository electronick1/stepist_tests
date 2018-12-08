import pytest

from collections import Counter


STOP_WORDS = ['a', 'the', 'on', 'at']


@pytest.fixture()
def simple_flow(app):
    @app.step(None)
    def return_amount_of_the(counts):
        return dict(the=counts['the'])

    @app.step(return_amount_of_the)
    def calculate_amount_of_stop_words(words):
        return dict(counts=Counter(words))

    @app.step(calculate_amount_of_stop_words)
    def split_by_words(text):
        return dict(words=text.split(' '),
                    text=text)

    @app.step(split_by_words)
    def read_text(file):
        with open(file, "r") as f:
            return dict(text=f.read())

    return read_text
