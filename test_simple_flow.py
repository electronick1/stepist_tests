import os

from stepist import just_do_it

from .test_flows import simple_flow, simple_worker_flow
from . import utils


def test_simple_flow():
    text_file_path = os.path.join(utils.get_test_data_path(),
                                  'game_of_thrones.txt')
    result = simple_flow.read_text(file=text_file_path)

    assert result['the'] == 73


def test_simple_worker_flow(redis_tests):
    text_file_path = os.path.join(utils.get_test_data_path(),
                                  'game_of_thrones.txt')
    result = simple_worker_flow.read_text(file=text_file_path)

    just_do_it(1, die_when_empty=True)

    print(utils.get_test_result())
    assert utils.get_test_result()['the'] == 73