from dataclasses import dataclass
from typing import Any, Optional, Hashable

from jsonschema.validators import validator_for

from src.domain.model.schema_base import SchemaBase


@dataclass
class Schema(SchemaBase):
    """Schema model for the database."""
    current_schema_definition: dict
    schema_id: Optional[str] = None
    current_version: Optional[Hashable] = None

    def __post_init__(self):
        """Post-initialization method to validate the schema name and definition."""
        self.validate_version(self.current_version)
        self.validate_schema_definition(self.current_schema_definition)

    @staticmethod
    def validate_schema_definition(val: Any):
        """Validate the schema definition."""
        if not isinstance(val, dict):
            raise ValueError("schema definition must be a dictionary")
        if not val:
            raise ValueError("schema definition must not be empty")
        validator_class = validator_for(val)
        validator_class.check_schema(val)

    @staticmethod
    def validate_version(val: Any):
        """Validate the schema version."""
        if not isinstance(val, int):
            val = 1
        if val < 1:
            raise ValueError("version must be greater than 0")
