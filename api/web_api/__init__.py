from flask import Flask

app = Flask(__name__)

from api.web_api import routes
