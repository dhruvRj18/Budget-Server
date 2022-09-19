import hashlib
import logging
from copy import copy
from http import HTTPStatus
from typing import Tuple

from flasgger import SwaggerView
from flask import Response, request, abort, jsonify
from marshmallow import ValidationError

from budget_server.data_manager import create_user, get_users, delete_user, get_user_by_id, update_user_by_id
from budget_server.schema import UserCreateSchema, user_create_schema, user_return_schema

log = logging.getLogger(__name__)

class UserViewBase(SwaggerView):
    tags = ['Users']

class UserCreate(UserViewBase):
    parameters = [
        {

            'in': 'body',
            'name': 'body',
            'required': True,
            'schema': UserCreateSchema,
            'description': 'Details of new client to create',

        },
    ]
    responses = {
        HTTPStatus.OK.value:{
            'description': 'A User',
        },
        HTTPStatus.UNPROCESSABLE_ENTITY.value:{
            'description': 'Unprocessable entity',
        },
    }

    def post(self) -> Tuple [Response,HTTPStatus]:
        payload = copy(request.json)
        pasString = payload['password']
        payload["password"] = hashlib.new("sha1",pasString.encode()).hexdigest()
        try:
            user_create_schema.load(payload)
        except ValidationError as e:
            abort(
                status=HTTPStatus.UNPROCESSABLE_ENTITY,
                description='One or more invalid fields in body',
            )
        user = create_user(payload)
        log.info(f'Added user : {user}')
        user_dump = user_return_schema.dump(user)
        return jsonify(user_dump), HTTPStatus.OK


class GetUsers(UserViewBase):
    responses = {
        HTTPStatus.OK.value: {
            'description': 'A User',
        },
    }

    def get(self):
        try:
            user = get_users()
            return jsonify(user), HTTPStatus.OK
        except:
            return None


class DeleteUser(UserViewBase):
    parameters = [
        {

            'in': 'path',
            'name': 'user_id',
            'required': True,
            'description': 'User Id of the user',

        },
    ]
    responses = {
        HTTPStatus.OK.value: {
            'description': 'A User',
        },
        HTTPStatus.UNPROCESSABLE_ENTITY.value: {
            'description': 'Unprocessable entity',
        },
    }

    def delete(self,user_id:str) -> Tuple[Response,HTTPStatus]:
        try:
            user = get_user_by_id(user_id)
            delete_user(user)
            user_dump = user_return_schema.dump(user)
            return jsonify(user_dump), HTTPStatus.OK
        except Exception as e:
            print(e)
            return None

class GetUser(UserViewBase):
    parameters = [
        {
            'in' : 'path',
            'name' : 'user_id',
            'required' : True,
            'description' : 'Get user by Id'
        },
    ]
    responses =  {
        HTTPStatus.OK.value:{
            'description' : 'A user from id',
        }
    }

    def get(self, user_id:str)->Tuple[Response,HTTPStatus]:
        user = get_user_by_id(user_id)
        return jsonify(user), HTTPStatus.OK

class UpdateUser(UserViewBase):
        parameters = [{
            'in': 'path',
            'name': 'user_id',
            'required': True,
            'description': 'Get user by Id to update'
        },
            {
                'in': 'body',
                'name': 'body',
                'required': True,
                'description': 'Enter user to update',
                'schema': UserCreateSchema
            }
        ]
        responses = {
            HTTPStatus.OK.value: {
                'description': 'A user from id is updated',
            }
        }

        def post(self, user_id: str):
            _user = get_user_by_id(user_id)
            payload = request.json
            try:
                user_create_schema.load(payload)
            except ValidationError as e:
                abort(
                    status=HTTPStatus.UNPROCESSABLE_ENTITY,
                    description='One or more invalid fields in body',
                )
            updated_user = update_user_by_id(_user, payload)
            user_dump = user_return_schema.dump(updated_user)
            return jsonify(user_dump), HTTPStatus.OK

























