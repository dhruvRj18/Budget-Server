import logging
from copy import copy
from http import HTTPStatus
from typing import Tuple

from flasgger import SwaggerView
from flask import Response, request, abort, jsonify
from marshmallow import ValidationError

from budget_server.data_manager import create_budget
from budget_server.data_manager.budget import read_budget_entries, read_budget_by_id, delete_budget
from budget_server.schema import create_budget_schema, budget_return_schema, CreateBudgetSchema

log = logging.getLogger(__name__)


class BudgetViewBase(SwaggerView):
    tags = ['Budget']


class CreateBudgetEntry(BudgetViewBase):
    parameters = [
        {
            'in': 'body',
            'name': 'body',
            'schema': CreateBudgetSchema,
            'description': 'Details of new Budget Entry to create',

        },
    ]
    responses = {
        HTTPStatus.OK.value: {
            'description': 'A Budget Entry',
        },
        HTTPStatus.UNPROCESSABLE_ENTITY.value: {
            'description': 'Unprocessable entity',
        },
    }

    def post(self) -> Tuple [Response, HTTPStatus]:
        payload = copy(request.json)
        try:
            create_budget_schema.load(payload)
        except ValidationError as e:
            abort(
                HTTPStatus.UNPROCESSABLE_ENTITY,
                description =f'One or more invalid fields in body, {e}',
            )
        budget = create_budget(payload)
        log.info(f'Added Budget Entry: {budget}')
        budget_dump = budget_return_schema.dump(budget)
        return jsonify(budget_dump),HTTPStatus.OK

class GetBudgets(BudgetViewBase):
    responses = {
        HTTPStatus.OK.value:{
            'description' : 'List of Budget',
        }
    }

    def get(self):
        try:
            budget = read_budget_entries()
            return jsonify(budget), HTTPStatus.OK
        except:
            return None


class GetBudget(BudgetViewBase):
    parameters = [
        {
            'in': 'path',
            'name': 'budget_id',
            'required': True,
            'description': 'Get budget by Id'
        },
    ]
    responses = {
        HTTPStatus.OK.value: {
            'description': 'A budget from id',
        }
    }

    def get(self,budget_id:str)-> Tuple[Response,HTTPStatus]:
        budget = read_budget_by_id(budget_id)
        return jsonify(budget), HTTPStatus.OK


class DeleteBudget(BudgetViewBase):
    parameters = [
        {
            'in': 'path',
            'name': 'budget_id',
            'required': True,
            'description': 'Budget Id of the budget entry',

        },
    ]
    responses = {
        HTTPStatus.OK.value: {
            'description': 'A Budget entry deleted',
        },
        HTTPStatus.UNPROCESSABLE_ENTITY.value: {
            'description': 'Unprocessable entity',
        },
    }

    def delete(self,budget_id) ->  Tuple[Response,HTTPStatus]:
        try:
            budget = read_budget_by_id(budget_id)
            delete_budget(budget)
            budget_dump = budget_return_schema.dump(budget)
            return jsonify(budget_dump), HTTPStatus.OK
        except Exception as e:
            log.error(e)
            return None
















