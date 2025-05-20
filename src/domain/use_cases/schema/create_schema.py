"""
Module for the CreateSchema use case.

This module defines the use case for creating a schema in the database.
It handles schema validation, creation, and rollback in case of errors.
"""

from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.external_interactions_errors import ExternalInteractionError

from src.domain.model.schema import Schema
from src.domain.model.schema_definition_version import SchemaDefinitionVersion


class CreateSchema(BasicUseCase):
    """Use case for creating a schema in the database."""


    def use(self, schema_info: dict, *args, **kwargs):
        """Create a new schema in the database."""

        # this implies validation of the schema_info
        schema = Schema(**schema_info)

        schema_def_version = SchemaDefinitionVersion(
            schema_keyname=schema.schema_keyname, schema_definition=schema.current_schema_definition
        )

        uid_schema_def_version = db.schema_def_version.create_schema_version(schema_def_version)

        self.log.info("Schema version was successfully created",
                      checkpoint_id="schema-version-created")

        schema.current_version = uid_schema_def_version
        try:
            uid_schema = db.schema.create_schema(schema)

            self.log.info(f"Schema was successfully created uid: {uid_schema}",
                          checkpoint_id="schema-saved")
        except ExternalInteractionError as err:

            self.log.error("Schema was not successfully created: " + str(err),
                           checkpoint_id="schema-catcher")
            db.schema.delete_schema(schema.schema_keyname)
            db.schema_def_version.delete_schema_version(uid_schema_def_version)

            self.log.info("Schema version was successfully deleted as a rollback",
                          checkpoint_id="schema-version-deleted-rollback")
            raise err

        store_created = db.stores.create_store_of_schema(schema)
        if store_created:
            self.log.info("Schema was successfully created",
                          checkpoint_id="store-of-schema-created")
        else:
            self.log.error("Schema was not successfully created",
                           checkpoint_id="store-of-schema-created-catcher")
            db.schema.delete_schema(schema.schema_keyname)
            db.schema_def_version.delete_schema_version(uid_schema_def_version)

            self.log.info("Schema was successfully deleted as a rollback",
                          checkpoint_id="schema-deleted-rollback")

        return {"schema": schema}


CREATE_SCHEMA = CreateSchema()
