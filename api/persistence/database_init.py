from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists
import pymssql
import api.persistence.base as base_model
from sqlalchemy.orm import sessionmaker
from api.persistence.models import *


class DatabaseInitialization:
    class DatabaseInitInternal:
        def __init__(self):
            self._engine = None
            self.init_database()

        def create_database(self, server, db_name):
            connection = pymssql.connect(server)
            connection.autocommit(True)
            cursor = connection.cursor()
            cursor.execute('CREATE DATABASE {0}'.format(db_name))
            connection.autocommit(False)

        def init_database(self):
            db_name = 'WhoDoIRemindOfDB'
            server = 'localhost'
            url = 'mssql+pymssql://{0}/{1}'.format(server, db_name)

            if not database_exists(url):
                self.create_database(server, db_name)

            self._engine = create_engine(url)
            metadata = MetaData(self._engine)
            base_model.Base.metadata.create_all(self._engine)
            DatabaseInitialization.create_session = sessionmaker(bind=self._engine)

    instance = None
    create_session = None

    def __init__(self):
        if not DatabaseInitialization.instance:
            DatabaseInitialization.instance = self.DatabaseInitInternal()
