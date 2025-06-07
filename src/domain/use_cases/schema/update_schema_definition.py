from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.domain_exception import NotFound

from src.domain.model.schema import Schema
from src.domain.model.schema_definition_version import SchemaDefinitionVersion


class UpdateSchemaDefinition(BasicUseCase):
    """
    Use case for updating the definition of a schema.
    """

    def use(self, schema_keyname: str, schema_definition: dict, *args, **kwargs):
        """Updates the definition of an existing schema in the database.

        Parameters
        ----------
        schema_keyname: str
            The name of the schema to be updated.
        schema_definition: dict
            The new definition for the schema.
        *args
            Positional arguments for the use case.
        **kwargs
            Keyword arguments for the use case.

        Returns
        -------
        bool
            True if the schema was updated successfully, False otherwise.
        """

        Schema.validate_schema_definition(schema_definition)

        schema = db.schema.get_schema(schema_keyname)

        if not schema:
            raise NotFound("schema-not-found", f"Schema with keyname '{schema_keyname}' not found.")

        schema_def_version = SchemaDefinitionVersion(schema_keyname, schema_definition)
        uid_schema_version = db.schema.create_schema_version(schema_def_version)

        uid_schema = db.schema.update_schema_definition(
            schema_keyname, new_version=uid_schema_version, definition=schema_definition)

        if not uid_schema:
            raise NotFound("schema-not-found", f"Schema with keyname '{schema_keyname}' not found.")

        return {"updated": uid_schema}
