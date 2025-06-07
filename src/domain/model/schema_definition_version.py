from collections.abc import Hashable
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class SchemaDefinitionVersion:
    """SchemaVersion model for the database.

    Attributes
    ----------
    schema_version_id : str
        The unique identifier for the schema version.
    schema_keyname : str
        The key name identifier of the schema.
    schema_definition : dict
        The definition of the schema.
    created_at : datetime
        The date and time when the schema version was created.
    """
    schema_keyname: str
    schema_definition: dict
    created_at: datetime = datetime.now()
    schema_version_id: Optional[Hashable] = None
