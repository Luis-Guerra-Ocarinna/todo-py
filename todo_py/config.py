
from .extensions.configuration import init_app as init_configuration
from .blueprints import init_app as init_blueprints


def init_app(app):
    app = (app
           | init_configuration
           | init_blueprints
           )
