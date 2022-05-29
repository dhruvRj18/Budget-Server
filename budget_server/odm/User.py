from budget_server import db

class User(db.Document):
    meta = {
        'strict' : True,
        'collection' : 'users',
    }

    email = db.StringField()
    name = db.StringField()
    profileImageFilePath = db.StringField()
    bankName = db.StringField()
    initialBalance = db.DecimalField()
    primaryBank = db.BooleanField()
    currentBalance = db.DecimalField()

