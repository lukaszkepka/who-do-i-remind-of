from flask import Flask
from api.persistence.database_init import DatabaseConfig

app = Flask(__name__)
DatabaseConfig.config(app)

from api.web_api import routes
