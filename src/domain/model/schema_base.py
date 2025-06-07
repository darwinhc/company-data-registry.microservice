from dataclasses import dataclass
from typing import Any


@dataclass
class SchemaBase:
    """SchemaMetadata model for the database.

    Attributes
    ----------
    schema_keyname : str
        The key name identifier of the schema.
    schema_name : str
        The name of the schema.
    schema_description : str
        The description of the schema.
    """
    schema_keyname: str
    schema_name: str
    schema_description: str

    def __post_init__(self):
        """Post-initialization method to validate the schema keyname, name, and description."""
        self.validate_schema_keyname(self.schema_keyname)
        self.validate_schema_name(self.schema_name)
        self.validate_schema_description(self.schema_description)

    def validate_schema_name(self, val: Any):
        """Validate the schema name."""
        self._validate_str_prop("schema_name", val)

    def validate_schema_description(self, val: Any):
        """Validate the schema description."""
        self._validate_str_prop("schema_description", val, min_length=10, max_length=255)

    @staticmethod
    def _validate_str_prop(field_name: str, val: Any, min_length: int = 3, max_length: int = 50):
        """Validate the schema name."""
        if not isinstance(val, str):
            raise ValueError(f"'{field_name}' must be a string")
        n_str = len(val)
        if n_str < min_length:
            raise ValueError(f"'{field_name}' must be at least {min_length} characters long: "
                             f"{n_str}")
        if n_str > max_length:
            raise ValueError(f"'{field_name}' must be at most {max_length} characters long: {n_str}")

    @classmethod
    def validate_schema_keyname(cls, val: Any):
        """Validate the schema keyname"""
        cls._validate_str_identifier("schema_keyname", val)

    @classmethod
    def _validate_str_identifier(cls, field_name: str, value: Any):
        """Validate the str identifier."""
        cls._validate_str_prop(field_name, value, min_length=3, max_length=50)
        value = value.strip().lower()
        if not value.isidentifier():
            raise ValueError(f"{field_name} must be a valid identifier")
