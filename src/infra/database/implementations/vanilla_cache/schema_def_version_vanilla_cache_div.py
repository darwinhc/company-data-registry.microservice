from collections.abc import Hashable
from datetime import timedelta, datetime
from typing import List, Optional, Dict
import uuid

from src.domain.model.schema_definition_version import SchemaDefinitionVersion
from src.infra.database.schema_def_version_division import SchemaDefVersionDivision


class SchemaDefVersionVanillaCacheDiv(SchemaDefVersionDivision):

    """
    In-memory implementation of the SchemaDefVersionDivision interface.

    This class manages schema definition versions using Python dictionaries,
    providing a simple cache mechanism for testing or non-persistent use cases.
    """

    def __init__(self):
        self._schema_versions : Dict[Hashable, SchemaDefinitionVersion] = {}



    def create_schema_version(self, schema_version: SchemaDefinitionVersion) -> Hashable:
        """
        Create a new schema version in the cache.

        Parameters
        ----------
        schema_version : SchemaDefinitionVersion
            The schema version instance to create.

        Returns
        -------
        Hashable
            The unique identifier of the created schema version.
        """
        uid = str(uuid.uuid4())
        schema_version.schema_id = uid
        self._schema_versions[uid] = schema_version
        return uid

    def get_schema_version(self, uid: Hashable) -> Optional[SchemaDefinitionVersion]:
        """
        Retrieve a schema version by its unique identifier.

        Parameters
        ----------
        uid : Hashable
            The unique identifier of the schema version.

        Returns
        -------
        Optional[SchemaDefinitionVersion]
            The schema version instance if found, otherwise None.
        """
        return self._schema_versions.get(uid)

    def get_schema_versions(self, schema_keyname: str) -> List[SchemaDefinitionVersion]:
        """
        List all versions of a specific schema.

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema whose versions are to be listed.

        Returns
        -------
        List[SchemaDefinitionVersion]
            List of schema version instances for the specified schema.
        """
        return [v for v in self._schema_versions.values() if v.schema_keyname == schema_keyname]

    def delete_schema_version(self, uid: Hashable) -> Hashable:
        """
        Delete a specific schema version from the cache.

        Parameters
        ----------
        uid : Hashable
            The unique identifier of the schema version to delete.

        Returns
        -------
        Hashable
            The unique identifier of the deleted schema version.
        """
        return self._schema_versions.pop(uid)

    def delete_inactive_schema_versions(self, schema_keyname: str,
                                        current_version: Hashable, days: int) -> List[Hashable]:
        """Delete all inactive versions of a specific schema.

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema whose inactive versions are to be deleted.
        current_version : Hashable
            The unique identifier of the current active schema version.
        days : int
            The number of days to consider a version as inactive.

        Returns
        -------
        List[Hashable]
            List of unique identifiers of the deleted schema versions.
        """
        deleted_uids = []
        for uid, version in list(self._schema_versions.items()):
            if (version.schema_keyname == schema_keyname and uid != current_version and
                    version.created_at < (datetime.now() - timedelta(days=days))):
                deleted_uids.append(uid)
                del self._schema_versions[uid]
        return deleted_uids
