"""
Module for the DeleteSchema use case.

This module defines the use case for deleting a schema from the database.
It handles the deletion process and logs the operation's success or failure.
"""
from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.domain_exception import NotFound



class DeleteSchema(BasicUseCase):
    """Use case for deleting a schema from the database."""

    def use(self, schema_keyname: str, *args, **kwargs):
        """Delete a schema from the database.

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema to delete.
        *args
            Positional arguments for the use case.
        **kwargs
            Keyword arguments for the use case.

        Returns
        -------
        bool
            True if the schema was deleted successfully, False otherwise.
        """
        uid_schema = db.schema.delete_schema(schema_keyname)
        if uid_schema:
            self.log.info(f"Schema with keyname '{schema_keyname}' was successfully deleted.",
                          checkpoint_id="schema-deleted")
        else:
            self.log.error(f"Schema with keyname '{schema_keyname}' was not found.",
                           checkpoint_id="schema-not-found")
            raise NotFound("schema-not-found", f"Schema with keyname '{schema_keyname}' not found.")
        return {"deleted": uid_schema}
