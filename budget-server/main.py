import logging
import os

from flasgger import Swagger
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo

from .constants import (
LOG_LEVEL,
MONGO_URI
)

log_level = os.environ.get(LOG_LEVEL,'WARNING')
log_level = getattr(logging,log_level)
logging_format = '%(asctime)s000 %(levelname)s [%(name)s] %(message)s'
logging_config = {
    'format' : logging_format,
    'level' : log_level,
}

logging.basicConfig(**logging_config)

log = logging.getLogger('budget-server')
log.info('*****Starting Budget Server*****')
log.debug('Create application')

application = Flask(__name__)

log.debug('environment settings')
application.config.update({
    'MONGO_URI':os.environ.get(MONGO_URI)
})

log.debug('open cors')
cors = CORS(application,resources={r'/api/*': {'origins':'*'}})

log.debug('JWT MAnager')
jwt = JWTManager(application)

log.debug('Load Database')
mongo = PyMongo(application)

log.debug('Load Api')

application.config['SWAGGER'] = {
    'title': 'Budget Server APIs',
    'version' : '0.0.1',
    'swagger' : '2.0',
    'swagger_ui' : True,
}

swagger = Swagger(application)

application.config['MONGODB_SETTINGS'] = {
    'host' : os.environ[MONGO_URI]
}



















