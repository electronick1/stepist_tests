import threading
import pytest

from stepist import config
from . import utils


@pytest.fixture()
def celery_engine():
    pass


@pytest.fixture()
def simple_queue_engine():
    pass


@pytest.fixture()
def redis_tests():
    utils.setup_redis_tests(**config.redis_kwargs)