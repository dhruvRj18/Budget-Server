from budget_server import db

class User(db.Document):
    meta = {
        'strict' : True,
        'collection' : 'users',
    }

    email = db.StringField()
    password = db.StringField()
    display_name = db.StringField()
    image_url = db.StringField()
    bank_name = db.StringField()
    initial_balance = db.DecimalField()
    primary_bank = db.BooleanField()
    contact = db.StringField()
    current_balance = db.DecimalField()

