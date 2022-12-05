from flask import Blueprint, Flask

from todo_py.web import hello_word

web = Blueprint(
    'web',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/web/static',)

web.register_blueprint(hello_word.bp)


def create_app():
    app = Flask(__name__)

    return app
