from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists
import pymssql
import api.persistence.base as base_model
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy_session import flask_scoped_session
from api.persistence.models import *


class DatabaseConfig:
    session_factory = None

    @staticmethod
    def create_database(server, db_name):
        connection = pymssql.connect(server)
        connection.autocommit(True)
        cursor = connection.cursor()
        cursor.execute('CREATE DATABASE {0}'.format(db_name))
        connection.autocommit(False)

    @staticmethod
    def init_database():
        db_name = 'WhoDoIRemindOfDB'
        server = 'localhost'
        url = 'mssql+pymssql://{0}/{1}'.format(server, db_name)

        if not database_exists(url):
            DatabaseConfig.create_database(server, db_name)

        engine = create_engine(url, deprecate_large_types=True)
        base_model.Base.metadata.create_all(engine)
        return engine

    @staticmethod
    def create_session_factory(db_engine, flask_app):
        DatabaseConfig.session_factory = flask_scoped_session(sessionmaker(bind=db_engine), flask_app)

    @staticmethod
    def config(flask_app):
        engine = DatabaseConfig.init_database()
        DatabaseConfig.create_session_factory(engine, flask_app)
