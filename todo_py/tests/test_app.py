from todo_py import api, web


def test_apps(app):
    assert app.blueprints['api'] is api
    assert app.blueprints['web'] is web

def test_url_prefixes(app):
    assert app.blueprints['api'].url_prefix == '/api'
    assert app.blueprints['web'].url_prefix is None
