from flask import Blueprint, Flask

from todo_py.api import hello_word

api = Blueprint('api', __name__, url_prefix='/api')

api.register_blueprint(hello_word.bp)


def create_app():
    app = Flask(__name__)

    app.add_url_rule('/', endpoint='api.hw.index')

    return app
