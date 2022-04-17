from flask_marshmallow import fields
from budget_server import ma

class UserCreateSchema(ma.Schema):
    email = fields.fields.String(required=True)
    password = fields.fields.String(required=True)
    display_name = fields.fields.String()
    image_url = fields.fields.String()
    bank_name = fields.fields.String()
    initial_balance = fields.fields.Decimal()
    primary_bank = fields.fields.Boolean()
    contact = fields.fields.String()
    current_balance = fields.fields.Decimal()

class UserReturnSchema(ma.Schema):
    class Meta:
        fields = [
            '_id',
            'email',
            'password',
            'display_name',
            'image_url',
            'bank_name',
            'initial_balance',
            'primary_bank',
            'contact',
            'current_balance',
        ]

    _id = fields.fields.String(attribute = 'id')