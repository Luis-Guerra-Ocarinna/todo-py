from .app import FlaskApp

from . import config


def create_app():
    app = FlaskApp(__name__)

    config.init_app(app)

    return app
