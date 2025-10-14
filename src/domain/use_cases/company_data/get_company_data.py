"""Get Company Data Use Case definition."""

from typing import Optional

from bisslog import BasicUseCase, bisslog_db as db


class GetCompanyData(BasicUseCase):
    """Get Company Data"""

    def use(self, schema_keyname: str, *, params: Optional[dict] = None, **__):
        """
        Get all data from the store of the schema in the database.

        Parameters
        ----------
        schema_keyname: str
            The name of the schema whose store is to be accessed.
        params : dict, optional
            Parameters to filter the data to be retrieved. If None, all data will be retrieved.
        __ : dict
            Keyword arguments.

        Returns
        -------
        dict
            A list of dictionaries, each containing information about a record in the store.
        """

        return {"data": db.stores.get_data_from_store(schema_keyname, params)}
