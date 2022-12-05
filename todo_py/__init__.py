from flask import Flask

from todo_py.api import api
from todo_py.web import web


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(web)

    return app
