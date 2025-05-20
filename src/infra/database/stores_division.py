from abc import ABCMeta, abstractmethod
from typing import Hashable, Optional, List

from bisslog import Division

from src.domain.model.schema import Schema


class StoresDivision(Division, metaclass=ABCMeta):
    """
    StoresDivision class to manage the stores division.
    """

    @abstractmethod
    def create_store_of_schema(self, schema: Schema) -> bool:
        """Create a new store for the schema in the database.

        Parameters
        ----------
        schema : Schema
            An instance of the Schema class defining the new store.

        Returns
        -------
        bool
            True if the store was created successfully, False otherwise.
        """
        raise NotImplementedError

    @abstractmethod
    def alter_store_of_schema(self, schema: Schema) -> bool:
        """Alter the store of the schema in the database.

        Parameters
        ----------
        schema : Schema
            An instance of the Schema class defining the new store.

        Returns
        -------
        bool
            True if the store was altered successfully, False otherwise.
        """
        raise NotImplementedError

    def get_one_data_from_store(self, schema_keyname: str, uid_data: Hashable) -> Optional[dict]:
        """Get one data from the store of the schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema whose store is to be accessed.
        uid_data : Hashable
            The unique identifier of the data to be retrieved.

        Returns
        -------
        dict
            A dictionary containing information about a record in the store.
        """
        raise NotImplementedError

    @abstractmethod
    def get_data_from_store(self, schema_keyname: str, params: dict) -> List[dict]:
        """Get data from the store of the schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema whose store is to be accessed.
        params : dict
            Parameters to filter the data.

        Returns
        -------
        list
            A list of dictionaries, each containing information about a record in the store.
        """
        raise NotImplementedError

    @abstractmethod
    def insert_data_into_store(self, schema_keyname: str, data: dict) -> Optional[Hashable]:
        """Insert data into the store of the schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema whose store is to be accessed.
        data : dict
            The validated data to be inserted into the store.

        Returns
        -------
        Hashable
            The unique identifier of the inserted data.
        """
        raise NotImplementedError

    @abstractmethod
    def update_data_in_store(self, schema_keyname: str, data: dict,
                             uid_data: Hashable) -> Optional[Hashable]:
        """Update data in the store of the schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema whose store is to be accessed.
        data : dict
            The validated data to be updated in the store.
        uid_data : Hashable
            The unique identifier of the data to be updated.

        Returns
        -------
        Hashable
            The unique identifier of the updated data.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_data_from_store(self, schema_keyname: str, uid_data: Hashable) -> Optional[Hashable]:
        """Delete data from the store of the schema in the database.

        Parameters
        ----------
        schema_keyname : str
            The name of the schema whose store is to be accessed.
        uid_data: Hashable
            The unique identifier of the data to be deleted.

        Returns
        -------
        Hashable
            The unique identifier of the deleted data.
        """
        raise NotImplementedError
