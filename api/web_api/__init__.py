from flask import Flask
from api.persistence.database_init import DatabaseInitialization

app = Flask(__name__)
db_init = DatabaseInitialization()

from api.web_api import routes
