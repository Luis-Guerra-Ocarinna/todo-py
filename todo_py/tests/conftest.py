# pylint: disable=redefined-outer-name
import tempfile
import pytest

from todo_py import create_app


@pytest.fixture()
def app():
    _, tmp_path = tempfile.mkstemp(prefix='todo_py-', suffix='-data.json')

    app = create_app(
        TESTING=True,
        STORAGE_FILE=tmp_path,
    )

    return app


@pytest.fixture()
def client(app):
    return app.test_client()
