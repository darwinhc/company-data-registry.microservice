from bisslog import BasicUseCase, bisslog_db as db

from src.domain.model.schema_base import SchemaBase


class UpdateSchemaMetadata(BasicUseCase):

    def use(self, schema_keyname: str, schema_new_info: dict, *args, **kwargs):
        """Updates the metadata of an existing schema in the database.

        Parameters
        ----------
        schema_keyname: str
            The name of the schema to be updated.
        schema_new_info: dict
            The new information for the schema.
        *args
            Positional arguments for the use case.
        **kwargs
            Keyword arguments for the use case.

        Returns
        -------
        bool
            True if the schema was updated successfully, False otherwise.
        """
        new_info_copy = schema_new_info.copy()
        new_info_copy["schema_keyname"] = schema_keyname

        schema = SchemaBase(**new_info_copy)

        uid_schema = db.schema.update_schema(schema)

        return {"updated": uid_schema}
