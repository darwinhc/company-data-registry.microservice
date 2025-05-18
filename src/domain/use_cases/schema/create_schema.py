"""
Module for the CreateSchema use case.

This module defines the use case for creating a schema in the database.
It handles schema validation, creation, and rollback in case of errors.
"""

from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.external_interactions_errors import ExternalInteractionError

from src.domain.model.schema import Schema


class CreateSchema(BasicUseCase):
    """Use case for creating a schema in the database."""


    def use(self, schema_info: dict, associate_info: dict, *args, **kwargs):
        """Create a new schema in the database.

        Parameters
        ----------
        schema_info : dict
            Schema information
        associate_info : dict
            User info to audit
        *args
            Positional arguments for the use case.
        **kwargs
            Keyword arguments for the use case.

        Returns
        -------
        bool
            True if the schema was created successfully, False otherwise.
        """

        # this implies validation of the schema_info
        schema = Schema(**schema_info)

        try:
            uid_schema = db.schema.create_schema(schema)

            self.log.info(f"Schema was successfully created uid: {uid_schema}",
                          checkpoint_id="schema-saved")
        except ExternalInteractionError as err:
            self.log.error("There was an error creating the schema: " + str(err),
                           checkpoint_id="schema-saved-catcher")
            raise err

        try:
            db.schema.create_store_of_schema(schema)
            self.log.info("Schema was successfully created",
                          checkpoint_id="store-of-schema-created")
        except ExternalInteractionError as err:
            self.log.error("Schema was not successfully created: " + str(err),
                           checkpoint_id="store-of-schema-created-catcher")
            db.schema.delete_schema(schema.schema_keyname)

            self.log.info("Schema was successfully deleted as a rollback",
                          checkpoint_id="schema-deleted-rollback")
            raise err

        return schema
