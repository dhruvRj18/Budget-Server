from .user import (
    UserCreateSchema,
    UserReturnSchema,
)

user_create_schema = UserCreateSchema()
user_return_schema = UserReturnSchema()
users_return_schema = UserReturnSchema(many=True)

__all__ = [
    users_return_schema,
    user_return_schema,
    user_create_schema,
]