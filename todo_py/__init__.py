from flask import Flask

from todo_py.api import api
from todo_py.web import web


def create_app(**config):
    app = Flask(__name__)

    app.config.from_mapping(
        STORAGE_FILE='data.json',
    )

    app.config.update(config)

    app.register_blueprint(api)
    app.register_blueprint(web)

    return app
