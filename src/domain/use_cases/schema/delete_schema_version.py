from typing import Hashable

from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.domain_exception import NotFound


class DeleteSchemaVersion(BasicUseCase):
    """
    Use case for updating the definition of a schema.
    """

    def use(self, uid_schema_def_version: Hashable, *args, **kwargs):
        """
        Updates the definition of an existing schema in the database.

        Parameters
        ----------
        uid_schema_def_version : Hashable
            Unique identifier of the schema definition version to be updated.
        *args
            Positional arguments for the use case.
        **kwargs
            Keyword arguments for the use case.

        Returns
        -------
        bool
            True if the schema was updated successfully, False otherwise.
        """
        uid_res = db.schema.delete_schema_version(uid_schema_def_version)
        if uid_res is None:
            raise NotFound("schema-version-not-found", "Schema definition version not found")
        return {"deleted": uid_res}
