from typing import Hashable

from bisslog import BasicUseCase, bisslog_db as db


class UpdateCompanyData(BasicUseCase):

    def use(self, schema_keyname:str, data: dict, uid_data: Hashable):
        """
        Update company data in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema to update data in.
        uid_data: Hashable
            The unique identifier of the data to be updated.
        data : dict
            The data to be updated in the schema.

        Returns
        -------
        dict
            A dictionary containing the result of the update operation.
        """
        uid_data = db.stores.update_data_in_store(schema_keyname, data, uid_data)
        return {"updated": uid_data}
