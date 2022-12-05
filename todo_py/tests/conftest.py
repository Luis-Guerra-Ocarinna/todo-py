# pylint: disable=redefined-outer-name
import pytest

from todo_py import create_app


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture()
def client(app):
    return app.test_client()
