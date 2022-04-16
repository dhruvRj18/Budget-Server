from flask_marshmallow import Marshmallow
from flask_mongoengine import MongoEngine

from .main import application

ma = Marshmallow(application)
db = MongoEngine()
db.init_app(application)