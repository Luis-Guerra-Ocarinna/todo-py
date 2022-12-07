from flask_login import LoginManager

from todo_py.repositories import user_repo

login_manager = LoginManager()
login_manager.login_view = 'web.auth.login'  # type: ignore


def init_app(app):
    login_manager.init_app(app)
    return app


@login_manager.user_loader
def load_user(user_id):
    return user_repo.get_by_username(username=user_id)
