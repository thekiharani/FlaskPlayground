from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/')
def api_index():
    return {'key': 'value'}
