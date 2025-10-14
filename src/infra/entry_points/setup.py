"""Setup entry point."""
import os

from bisslog import bisslog_db as db
from bisslog_schema.setup import bisslog_runtime_config
from pymongo import MongoClient
from pymongo.server_api import ServerApi

from src.infra.database.implementations.pymongo.schema_def_version_pymongo_div import (
    SchemaDefVersionMongoDivision
)
from src.infra.database.implementations.pymongo.schema_pymongo_division import SchemaMongoDivision
from src.infra.database.implementations.pymongo.stores_pymongo_div import StoreMongoDivision


@bisslog_runtime_config("flask", "fastapi", "lambda")
def setup():
    """Setup entry point for flask, fastapi, lambda."""
    uri = (f'mongodb+srv://{os.environ["MONGO_USER"]}:{os.environ["MONGO_PASS"]}@'
           f'{os.environ["MONGO_HOST"]}/?retryWrites=true&w=majority&appName=datikz-stage')
    print("uri", uri)
    conn = MongoClient(uri, server_api=ServerApi('1'))

    db_name = "company_data_registry"
    db.register_adapters(stores=StoreMongoDivision(conn, db_name),
                         schema=SchemaMongoDivision(conn, db_name),
                         schema_version=SchemaDefVersionMongoDivision(conn, db_name))
