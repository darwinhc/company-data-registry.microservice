from bisslog import BasicUseCase, bisslog_db as db


class GetAllSchemas(BasicUseCase):


    def use(self, *args, **kwargs):
        """Retrieve all schemas from the database.

        Returns
        -------
        list
            A list of all schemas in the database.
        """
        return db.schema.get_all_schemas()
