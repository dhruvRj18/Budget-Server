from budget_server import db


class Budget(db.Document):
    meta = {
        'strict' : True,
        'collection' : 'budget',
    }

    date = db.DecimalField()
    bankName = db.StringField()
    amount = db.DecimalField()
    creditOrDebit = db.BooleanField()