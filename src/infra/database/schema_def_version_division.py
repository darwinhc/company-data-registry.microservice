from abc import ABCMeta, abstractmethod
from collections.abc import Hashable
from typing import Optional, List

from bisslog import Division

from src.domain.model.schema_definition_version import SchemaDefinitionVersion


class SchemaDefVersionDivision(Division, metaclass=ABCMeta):
    """Class to handle schema definition version operations for the database division."""


    @abstractmethod
    def create_schema_version(self, schema_version: SchemaDefinitionVersion) -> Hashable:
        """Create a new version of a schema in the database.

        Parameters
        ----------
        schema_version : SchemaDefinitionVersion
            A dictionary defining the new version of the schema.

        Returns
        -------
        Hashable
            Unique identifier for the created schema version.
        """
        raise NotImplementedError

    @abstractmethod
    def get_schema_version(self, uid: Hashable) -> Optional[SchemaDefinitionVersion]:
        """Retrieve the version of a specific schema.

        Parameters
        ----------
        uid: Hashable
            Unique identifier of schema definition version

        Returns
        -------
        dict
            A dictionary containing the version information for the specified schema.
        """
        raise NotImplementedError

    @abstractmethod
    def get_schema_versions(self, schema_keyname: str) -> List[SchemaDefinitionVersion]:
        """List versions of a specific schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema whose versions are to be listed.

        Returns
        -------
        list[SchemaDefinitionVersion]
            A list of dictionaries, each containing information about a version of the specified schema.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_schema_version(self, uid: Hashable) -> Optional[Hashable]:
        """Delete a specific version of a schema from the database.

        Parameters
        ----------
        uid: Hashable
            Unique identifier of schema version

        Returns
        -------
        bool
            True if the schema version was deleted successfully, False otherwise.
        """
        raise NotImplementedError

