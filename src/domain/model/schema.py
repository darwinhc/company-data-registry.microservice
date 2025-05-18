from dataclasses import dataclass
from typing import Any

from jsonschema.validators import validator_for

@dataclass
class Schema:
    """Schema model for the database.

    Attributes
    ----------
    schema_name : str
        The name of the schema.
    current_schema_definition : dict
        The definition of the schema."""
    schema_name: str
    schema_keyname: str
    schema_identifier: str
    current_schema_definition: dict
    current_version: int = 1

    def __post_init__(self):
        """Post-initialization method to validate the schema name and definition."""
        self._validate_str_identifier("schema_keyname", self.schema_keyname)
        self._validate_schema_definition()
        self._validate_str_identifier("schema_identifier", self.schema_identifier)
        self._validate_schema_name()

    def _validate_schema_name(self):
        """Validate the schema name."""
        if not isinstance(self.schema_name, str):
            raise ValueError("schema_name must be a string")
        if len(self.schema_name) < 3:
            raise ValueError("schema_name must be at least 3 characters long: "
                             f"{len(self.schema_name)}")
        if len(self.schema_name) > 100:
            raise ValueError("schema_name must be at most 50 characters long: "
                             f"{len(self.schema_name)}")

    @staticmethod
    def _validate_str_identifier(field_name: str, value: Any):
        """Validate the str identifier."""
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a string")
        value = value.strip().lower()
        if not value.isidentifier():
            raise ValueError(f"{field_name} must be a valid identifier")
        if len(value) < 3:
            raise ValueError(f"{field_name} must be at least 3 characters long: "
                             f"{len(value)}")
        if len(value) > 50:
            raise ValueError(f"{field_name} must be at most 50 characters long: "
                             f"{len(value)}")

    def _validate_schema_definition(self):
        """Validate the schema definition."""
        if not isinstance(self.current_schema_definition, dict):
            raise ValueError("must be a dictionary")
        validator_class = validator_for(self.current_schema_definition)
        validator_class.check_schema(self.current_schema_definition)


    def _validate_version(self):
        """Validate the schema version."""
        if not isinstance(self.current_version, int):
            self.current_version = 1
        if self.current_version < 1:
            raise ValueError("version must be greater than 0")
