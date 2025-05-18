from dataclasses import dataclass
from datetime import datetime


@dataclass
class SchemaVersion:
    """SchemaVersion model for the database.

    Attributes
    ----------
    schema_version_id : str
        The unique identifier for the schema version.
    schema_keyname : str
        The key name identifier of the schema.
    version : int
        The version number of the schema.
    schema_definition : dict
        The definition of the schema.
    created_at : datetime
        The date and time when the schema version was created.
    """
    schema_version_id: str
    schema_keyname: str
    version: int
    schema_definition: dict
    created_at: datetime
