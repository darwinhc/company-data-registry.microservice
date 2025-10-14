"""Get all schemas use case definition"""
from bisslog import bisslog_db as db, use_case, AsyncBasicUseCase


class GetAllSchemas(AsyncBasicUseCase):
    """Get all schemas"""

    @use_case
    async def get_all_schemas_method(self, *_, **__):
        """Retrieve all schemas from the database.

        Returns
        -------
        list
            A list of all schemas in the database.
        """
        return db.schema.get_schemas()
