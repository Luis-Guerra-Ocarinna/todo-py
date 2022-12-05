from flask import Blueprint

bp = Blueprint('hw', __name__)


@bp.route('/')
def index():
    return {'message': 'Hello, World!'}
