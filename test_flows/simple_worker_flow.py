import pytest

from collections import Counter

from .. import utils

STOP_WORDS = ['a', 'the', 'on', 'at']


@pytest.fixture()
def simple_worker_flow(app):

    @app.step(None, as_worker=True)
    def save_to_redis(the):
        print("#33333")
        utils.save_test_result(dict(the=the))

    @app.step(save_to_redis)
    def return_amount_of_the(counts):
        return dict(the=counts['the'])

    @app.step(return_amount_of_the, as_worker=True)
    def calculate_amount_of_stop_words(words):
        print("#22222")
        return dict(counts=Counter(words))

    @app.step(calculate_amount_of_stop_words, as_worker=True)
    def split_by_words(text):
        print("#1111")
        return dict(words=text.split(' '),
                    text=text)

    @app.step(split_by_words)
    def read_text(file):
        with open(file, "r") as f:
            return dict(text=f.read())

    return read_text
