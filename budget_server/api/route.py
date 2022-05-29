import logging
from http import HTTPStatus

from flask import Blueprint,abort,jsonify

from budget_server.api import user,budget
from budget_server.api.budget import GetBudgets

log = logging.getLogger('route')
api_blueprint = Blueprint('api',__name__,url_prefix='/api')

def init_api_blueprint():
    return api_blueprint

# default for unrecognised routes is 404
@api_blueprint.route('/',defaults={'path':''})
@api_blueprint.route('/<path:path>')
def index(path):
    abort(HTTPStatus.NOT_FOUND)

#user endpoints

api_blueprint.add_url_rule(
    rule='/user',
    methods=['POST'],
    view_func=user.UserCreate.as_view('Create User')
)

api_blueprint.add_url_rule(
    rule='/user',
    methods=['GET'],
    view_func=user.GetUsers.as_view('Get Users')
)

api_blueprint.add_url_rule(
    rule='/user/<user_id>',
    methods=['GET'],
    view_func=user.GetUser.as_view('Get User')
)

api_blueprint.add_url_rule(
    rule='user/<user_id>',
    methods=['POST'],
    view_func=user.UpdateUser.as_view('user_update')
)


api_blueprint.add_url_rule(
    rule='/user/<user_id>',
    methods = ['DELETE'],
    view_func=user.DeleteUser.as_view('Delete User')
)

#budget entry endpoints

api_blueprint.add_url_rule(
    rule='/budget',
    methods=['POST'],
    view_func= budget.CreateBudgetEntry.as_view('Create Budget Entry')
)

api_blueprint.add_url_rule(
    rule='/budget',
    methods=['GET'],
    view_func= GetBudgets.as_view('Get all Budget Entries')
)

api_blueprint.add_url_rule(
    rule='/budget/<budget_id>',
    methods=['GET'],
    view_func=budget.GetBudget.as_view('Get budget entry by id')
)