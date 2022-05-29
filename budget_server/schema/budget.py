from flask_marshmallow import fields

from budget_server import ma


class CreateBudgetSchema(ma.Schema):
    date = fields.fields.Decimal(required=True)
    bankName = fields.fields.String(required=True)
    purpose = fields.fields.String(required=True)
    amount = fields.fields.Decimal(required=True)
    creditOrDebit = fields.fields.String(required=True)


class BudgetReturnScema(ma.Schema):
    class Meta:
        fields = [
            '_id',
            'date',
            'bankName',
            'purpose',
            'amount',
            'creditOrDebit',
        ]

    _id = fields.fields.String(attribute = 'id')