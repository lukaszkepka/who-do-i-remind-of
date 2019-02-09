from flask import Flask
from api.persistence.database_init import DatabaseConfig
from api.services.service_locator import ServiceLocator

app = Flask(__name__)

# Database configuration
DatabaseConfig.config(app)
# Services configuration
ServiceLocator = ServiceLocator()

from api.web_api import routes



