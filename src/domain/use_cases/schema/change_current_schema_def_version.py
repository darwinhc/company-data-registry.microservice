"""Change current schema definition version use case definition"""

from collections.abc import Hashable

from bisslog import bisslog_db as db, AsyncBasicUseCase
from bisslog.exceptions.domain_exception import NotFound

from src.domain.model.schema_definition_version import SchemaDefinitionVersion


class ChangeCurrentSchemaDefVersion(AsyncBasicUseCase):
    """Change current schema definition version."""

    async def use(self, schema_keyname: str, uid_schema_version: Hashable, *_, **__):
        """
        Change the current schema definition version for an existing different version.

        Parameters
        ----------
        schema_keyname : str
            The key name of the schema definition.
        uid_schema_version : Hashable
            The unique identifier of the schema version to be set as current.
        """
        self.log.info("Changing current schema definition version "
                      f"for {schema_keyname} to {uid_schema_version}")

        schema_version: SchemaDefinitionVersion = db.schema.get_schema_version(uid_schema_version)
        if not schema_version:
            raise NotFound("schema-version-not-found",
                           f"Schema version {uid_schema_version} not found.")

        uid_schema = db.schema.update_schema_definition(
            schema_keyname=schema_keyname, new_version=uid_schema_version,
            definition=schema_version.schema_definition)
        if not uid_schema:
            raise NotFound("schema-not-found", f"Schema {schema_keyname} not found.")

        return {"updated_schema": uid_schema, "schema_version": uid_schema_version}


CHANGE_CURRENT_SCHEMA_DEF_VERSION = ChangeCurrentSchemaDefVersion()
