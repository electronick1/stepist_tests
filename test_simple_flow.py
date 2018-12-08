import os

from . import utils


def test_simple_flow(simple_flow):
    text_file_path = os.path.join(utils.get_test_data_path(),
                                  'game_of_thrones.txt')
    result = simple_flow(file=text_file_path)

    assert result['the'] == 73


def test_worker_flow(app, redis_db, simple_worker_flow):
    text_file_path = os.path.join(utils.get_test_data_path(),
                                  'game_of_thrones.txt')
    simple_worker_flow(file=text_file_path)
    utils.process_workers(app)

    result = utils.get_test_result()
    assert result['the'] == 73
