from bisslog import use_case, bisslog_db as db

from src.domain.model.schema import Schema


@use_case
def get_schema(schema_keyname: str) -> Schema:
    """Get schema by keyname"""
    return db.schema.get_schema(schema_keyname)
