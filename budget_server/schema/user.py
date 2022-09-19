from flask_marshmallow import fields
from budget_server import ma

class UserCreateSchema(ma.Schema):
    email = fields.fields.String(required=True)
    password = fields.fields.String(required=True)
    name = fields.fields.String()
    profileImageFilePath = fields.fields.String()
    bankName = fields.fields.String()
    initialBalance = fields.fields.Decimal()
    primaryBank = fields.fields.Boolean()
    currentBalance = fields.fields.Decimal()

class UserReturnSchema(ma.Schema):
    class Meta:
        fields = [
            '_id',
            'email',
            'password'
            'name',
            'profileImageFilePath',
            'bankName',
            'initialBalance',
            'primaryBank',
            'currentBalance',
        ]

    _id = fields.fields.String(attribute = 'id')