import pytest

from celery import Celery

from stepist.app import App
from stepist.flow.workers.adapters.celery_queue import CeleryAdapter
from . import utils


REDIS_KWARGS = dict(host='localhost', port=6379, decode_responses=True)


@pytest.fixture()
def app():
    return App()


@pytest.fixture()
def redis_app():
    return App()


@pytest.fixture()
def celery_app():
    app = App()

    celery = Celery(broker="redis://localhost:6379/0")
    app.worker_engine = CeleryAdapter(app,
                                      celery)

    return app

from .test_flows.simple_flow import *
from .test_flows.simple_worker_flow import *


@pytest.fixture()
def redis_db():
    return utils.setup_redis_tests(**REDIS_KWARGS)


def pytest_addoption(parser):
    parser.addoption("--app", action="append", default=[],
        help="list of stringinputs to pass to test functions")


def pytest_generate_tests(metafunc):
    if 'app' in metafunc.fixturenames and metafunc.config.getoption('app'):
        if metafunc.config.getoption('app')[0] == 'redis':
            metafunc.parametrize("app", [redis_app()])

        if metafunc.config.getoption('app')[0] == 'celery':
            metafunc.parametrize("app", [celery_app()])






