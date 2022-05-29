from budget_server import db


class Budget(db.Document):
    meta = {
        'strict' : True,
        'collection' : 'budget',
    }

    date = db.IntField()
    bankName = db.StringField()
    purpose = db.StringField()
    amount = db.DecimalField()
    creditOrDebit = db.StringField()