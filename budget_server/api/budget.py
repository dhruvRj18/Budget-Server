import logging
from copy import copy
from http import HTTPStatus
from typing import Tuple

from flasgger import SwaggerView
from flask import Response, request, abort, jsonify
from marshmallow import ValidationError

from budget_server.data_manager import create_budget
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


















