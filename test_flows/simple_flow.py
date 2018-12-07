from uuid import uuid4
from collections import Counter
from stepist import step


STOP_WORDS = ['a', 'the', 'on', 'at']


@step(None, unique_id=uuid4())
def return_amount_of_the(counts):
    return dict(the=counts['the'])


@step(return_amount_of_the, unique_id=uuid4())
def calculate_amount_of_stop_words(words):
    return dict(counts=Counter(words))


@step(calculate_amount_of_stop_words, unique_id=uuid4())
def split_by_words(text):
    return dict(words=text.split(' '),
                text=text)


@step(split_by_words, unique_id=uuid4())
def read_text(file):
    with open(file, "r") as f:
        return dict(text=f.read())