from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists
import pymssql
import api.persistence.base as base_model
from api.persistence.models import *


def create_database(server, db_name):
    connection = pymssql.connect(server)
    connection.autocommit(True)
    cursor = connection.cursor()
    cursor.execute('CREATE DATABASE {0}'.format(db_name))
    connection.autocommit(False)


db_name = 'WhoDoIRemindOfDB'
server = 'localhost'
url = 'mssql+pymssql://{0}/{1}'.format(server, db_name)

if not database_exists(url):
    create_database(server, db_name)

engine = create_engine(url)
metadata = MetaData(engine)
base_model.Base.metadata.create_all(engine)
