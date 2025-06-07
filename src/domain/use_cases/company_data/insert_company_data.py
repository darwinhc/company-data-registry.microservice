from bisslog import BasicUseCase, bisslog_db as db
from bisslog.exceptions.domain_exception import NotFound
from jsonschema.validators import Draft7Validator


class InsertCompanyData(BasicUseCase):
    """Class to insert company data into the database."""

    def use(self, schema_keyname: str, data: dict, *args, **kwargs) -> dict:
        """
        Insert company data into the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema to insert data into.
        data : dict
            The data to be inserted into the schema.
        args : tuple
            Positional arguments.
        kwargs : dict
            Keyword arguments.

        Returns
        -------
        dict:
            A dictionary containing the result of the insertion.
        """

        schema = db.schema.get_schema(schema_keyname)
        if not schema:
            raise NotFound("schema-not-found", f"Schema '{schema_keyname}' not found.")
        validator = Draft7Validator(schema.current_schema_definition)

        errors = list(validator.iter_errors(data))

        if errors:
            error_messages = [f"Error in '{error.instance}': {error.message}" for error in errors]

            return {"errors": error_messages}


        uid_data = db.stores.insert_data_into_store(schema_keyname, data)

        return {"inserted": uid_data}


INSERT_COMPANY_DATA = InsertCompanyData()
