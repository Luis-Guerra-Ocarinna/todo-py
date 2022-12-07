from flask import Blueprint

from .views.auth import auth
from .views.main import main

web = Blueprint('web', __name__,
                template_folder='templates',
                static_folder='static',
                static_url_path='/web/static')

web.register_blueprint(main)
web.register_blueprint(auth)


def init_app(app):
    app.register_blueprint(web)
    return app
