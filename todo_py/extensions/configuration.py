from dynaconf import FlaskDynaconf


def init_app(app):
    FlaskDynaconf(app, load_dotenv=True)
    return app
