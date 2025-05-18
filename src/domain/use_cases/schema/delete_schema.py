"""
Module for the DeleteSchema use case.

This module defines the use case for deleting a schema from the database.
It handles the deletion process and logs the operation's success or failure.
"""
from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.external_interactions_errors import ExternalInteractionError

from src.domain.model.user_info import UserInfo


class DeleteSchema(BasicUseCase):
    """Use case for deleting a schema from the database."""

    def use(self, schema_keyname: str, user_info: UserInfo, *args, **kwargs):
        """Delete a schema from the database.

        Parameters
        ----------
        schema_keyname : str
            The keyname of the schema to delete.
        user_info : UserInfo
            User info to audit.
        *args
            Positional arguments for the use case.
        **kwargs
            Keyword arguments for the use case.

        Returns
        -------
        bool
            True if the schema was deleted successfully, False otherwise.
        """
        try:
            db.schema.delete_schema(schema_keyname)
            self.log.info(f"Schema with keyname '{schema_keyname}' was successfully deleted.",
                          checkpoint_id="schema-deleted")
        except ExternalInteractionError as err:
            self.log.error(f"Error deleting schema with keyname '{schema_keyname}': {str(err)}",
                           checkpoint_id="schema-deletion-error")
            raise err

        return True
