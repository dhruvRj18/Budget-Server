import logging
from http import HTTPStatus

from flask import Blueprint,abort,jsonify

log = logging.getLogger('route')
api_blueprint = Blueprint('api',__name__,url_prefix='/api')

def init_api_blueprint():
    return api_blueprint

# default for unrecognised routes is 404
@api_blueprint.route('/',defaults={'path':''})
@api_blueprint.route('/<path:path>')
def index(path):
    abort(HTTPStatus.NOT_FOUND)
