import time
import os
import ujson
import redis

redis_tests = None


def process_workers(app):
    process_list = app.just_do_it(1, die_when_empty=True)
    time.sleep(2)
    for process in process_list:
        process.terminate()
        process.join()


def setup_redis_tests(**redis_kwargs):
    global redis_tests
    redis_tests = redis.Redis(**redis_kwargs)


def save_test_result(data):
    global redis_tests
    redis_tests.set("test_result",
                    ujson.dumps(data),
                    ex=30)


def get_test_result():
    global redis_tests

    test_result = redis_tests.get("test_result")
    if not test_result:
        return None

    return ujson.loads(test_result)


def get_test_data_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "test_data")
