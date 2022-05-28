from flask_marshmallow import fields

from budget_server import ma


class CreateBudgetSchema(ma.Schema):
    date = fields.fields.Decimal(required=True)
    bankName = fields.fields.String(required=True)
    amount = fields.fields.Decimal(required=True)
    creditOrDebit = fields.fields.Boolean(required=True)


class BudgetReturnScema(ma.Schema):
    class Meta:
        fields = [
            '_id',
            'date',
            'bankName',
            'amount',
            'creditOrDebit',
        ]

    _id = fields.fields.String(attribute = 'id')