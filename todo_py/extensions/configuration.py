from dynaconf import FlaskDynaconf


def init_app(app):
    # TODO: use .secrets.toml
    FlaskDynaconf(app)
    return app
