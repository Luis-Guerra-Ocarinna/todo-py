
from .blueprints import init_app as init_blueprints
from .extensions.authentication import init_app as init_authentication
from .extensions.configuration import init_app as init_configuration


def init_app(app):
    app = (app
           | init_configuration
           | init_blueprints
           | init_authentication
           )
