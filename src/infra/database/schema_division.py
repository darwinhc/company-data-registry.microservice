from abc import abstractmethod, ABCMeta
from typing import List

from bisslog import Division

from src.domain.model.schema import Schema


class SchemaDivision(Division, metaclass=ABCMeta):
    """Class to handle schema operations for the database division."""

    @abstractmethod
    def get_schema(self, schema_keyname: str) -> dict:
        """Retrieve the schema for a specific table.

        Parameters
        ----------
        schema_keyname : str
            The name of the table whose schema is to be retrieved.

        Returns
        -------
        dict
            A dictionary containing the schema information for the specified table.
        """
        raise NotImplementedError

    @abstractmethod
    def create_store_of_schema(self, schema: Schema) -> bool:
        """Create a new store for the schema in the database.

        Parameters
        ----------
        schema : Schema
            An instance of the Schema class defining the new store.

        Returns
        -------
        bool
            True if the store was created successfully, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def get_schemas(self, params: dict) -> List[Schema]:
        """List schemas in the database.

        Returns
        -------
        list
            A list of dictionaries, each containing information about a schema.
        """
        raise NotImplementedError

    @abstractmethod
    def create_schema(self, schema: Schema) -> str:
        """Create a new schema in the database.

        Parameters
        ----------
        schema : Schema
            An instance of the Schema class defining the new schema.

        Returns
        -------
        str
            Unique identifier for the created schema.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_schema(self, schema_keyname: str) -> bool:
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
    def update_schema(self, schema_keyname: str, schema_definition: dict) -> bool:
        """Update an existing schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema to be updated.
        schema_definition : dict
            A dictionary defining the new structure of the schema.

        Returns
        -------
        bool
            True if the schema was updated successfully, False otherwise.
        """
        raise NotImplementedError
