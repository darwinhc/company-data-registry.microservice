from abc import abstractmethod, ABCMeta
from collections.abc import Hashable
from typing import List, Optional

from bisslog import Division

from src.domain.model.schema import Schema
from src.domain.model.schema_base import SchemaBase


class SchemaDivision(Division, metaclass=ABCMeta):
    """Class to handle schema operations for the database division."""

    @abstractmethod
    def get_schema(self, schema_keyname: str) -> Optional[Schema]:
        """Retrieve the schema for a specific table.

        Parameters
        ----------
        schema_keyname : str
            The name of the table whose schema is to be retrieved.

        Returns
        -------
        Schema
            The schema information for the specified table.
        """
        raise NotImplementedError

    @abstractmethod
    def get_schemas(self, params: dict) -> List[Schema]:
        """List schemas in the database.

        Parameters
        ----------
        params : dict
            Parameters to filter the schemas.

        Returns
        -------
        list
            A list of dictionaries, each containing information about a schema.
        """
        raise NotImplementedError

    @abstractmethod
    def create_schema(self, schema: Schema) -> Hashable:
        """Create a new schema in the database.

        Parameters
        ----------
        schema : Schema
            An instance of the Schema class defining the new schema.

        Returns
        -------
        Hashable
            Unique identifier for the created schema.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_schema(self, schema_keyname: str) -> Optional[Hashable]:
        """Delete a schema from the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema to be deleted.

        Returns
        -------
        bool
            True if the schema was deleted successfully, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def update_schema(self, schema: SchemaBase) -> Optional[Hashable]:
        """Update an existing schema metadata in the database.
        Not the schema definition.

        Parameters
        ----------
        schema: SchemaBase
            Data with updated information.

        Returns
        -------
        str
            Unique identifier for the updated schema.
        """
        raise NotImplementedError


    @abstractmethod
    def update_schema_definition(self, schema_keyname: str, new_version: Hashable,
                                 definition: dict) -> Optional[Hashable]:
        """Update the definition of a schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema to be updated.
        new_version : Hashable
            The new version of the schema.
        definition : dict
            The new definition for the schema.

        Returns
        -------
        bool
            True if the schema was updated successfully, False otherwise.
        """
        raise NotImplementedError
