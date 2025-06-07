"""
Module for a vanilla in-memory cache implementation of the SchemaDivision interface.

This module provides a simple, non-persistent implementation of schema and schema version
management using Python dictionaries as in-memory stores.
"""

import uuid
from typing import Optional, List, Dict, Hashable

from src.domain.model.schema import Schema
from src.domain.model.schema_base import SchemaBase
from src.infra.database.schema_division import SchemaDivision


class SchemaVanillaCacheDivision(SchemaDivision):
    """
    In-memory implementation of the SchemaDivision interface.

    This class manages schemas and schema versions using Python dictionaries,
    providing a simple cache mechanism for testing or non-persistent use cases.
    """


    def __init__(self):
        """
        Initialize the in-memory stores for schemas and schema versions.
        """
        self._schemas : Dict[str, Schema] = {}

    def get_schema(self, schema_keyname: str) -> Optional[Schema]:
        """
        Retrieve a schema by its keyname.

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema to retrieve.

        Returns
        -------
        Optional[Schema]
            The schema instance if found, otherwise None.
        """
        return self._schemas.get(schema_keyname)

    def get_schemas(self, params: dict) -> List[Schema]:
        """
        List all schemas in the cache.

        Parameters
        ----------
        params : dict
            Parameters to filter the schemas (ignored in this implementation).

        Returns
        -------
        List[Schema]
            List of all schema instances in the cache.
        """
        return list(self._schemas.values())

    def create_schema(self, schema: Schema) -> str:
        """
        Create a new schema in the cache.

        Parameters
        ----------
        schema : Schema
            The schema instance to create.

        Returns
        -------
        str
            The unique identifier of the created schema.
        """
        schema.schema_id = str(uuid.uuid4())
        self._schemas[schema.schema_keyname] = schema
        return schema.schema_id

    def delete_schema(self, schema_keyname: str) -> Optional[Hashable]:
        """
        Delete a schema from the cache.

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema to delete.

        Returns
        -------
        Optional[Hashable]
            The unique identifier of the deleted schema, or None if not found.
        """
        res = self._schemas.pop(schema_keyname, None)
        if res is None:
            return None
        return res.schema_id

    def update_schema(self, schema: SchemaBase) -> Optional[Hashable]:
        """
        Update the metadata of an existing schema in the cache.

        Parameters
        ----------
        schema : SchemaBase
            The schema base instance with updated information.

        Returns
        -------
        Optional[Hashable]
            The unique identifier of the updated schema, or None if not found.
        """
        if schema.schema_keyname not in self._schemas:
            return None
        self._schemas[schema.schema_keyname].schema_name = schema.schema_name
        self._schemas[schema.schema_keyname].schema_description = schema.schema_description
        return self._schemas[schema.schema_keyname].schema_id



    def update_schema_definition(self, schema_keyname: str, new_version: Hashable,
                                 definition: dict) -> Optional[Hashable]:
        """Update schema definition on schema

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema to update.
        new_version : Hashable
            The new version identifier for the schema.
        definition : dict
            The new schema definition to set.
        """
        if schema_keyname not in self._schemas:
            return None
        self._schemas[schema_keyname].current_schema_definition = definition
        return self._schemas[schema_keyname].schema_id
