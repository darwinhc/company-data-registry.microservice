import uuid
from typing import List, Hashable, Optional

from bisslog.exceptions.domain_exception import NotFound

from src.domain.model.schema import Schema
from src.infra.database.stores_division import StoresDivision


class StoresVanillaCacheDivision(StoresDivision):
    """
    In-memory implementation of the StoresDivision interface.

    This class manages stores using Python dictionaries,
    providing a simple cache mechanism for testing or non-persistent use cases.
    """



    def __init__(self):
        """
        Initialize the in-memory store for stores.
        """
        self._stores = {}

    def create_store_of_schema(self, schema: Schema) -> bool:
        """
        Create a new store for the schema in the cache.

        Parameters
        ----------
        schema : Schema
            The schema instance to create a store for.

        Returns
        -------
        bool
            Always True, as this is a no-op in the cache implementation.
        """
        self._stores[schema.schema_keyname] = {}
        return True

    def alter_store_of_schema(self, schema: Schema) -> bool:
        """
        Alter the store of the schema in the cache.

        Parameters
        ----------
        schema : Schema
            The schema instance to alter the store for.

        Returns
        -------
        bool
            Always True, as this is a no-op in the cache implementation.
        """
        return True

    def get_one_data_from_store(self, schema_keyname: str, uid_data: Hashable) -> Optional[dict]:
        """
        Get one data from the store of the schema in the cache.

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
        return self._stores.get(schema_keyname, {}).get(uid_data)

    def get_data_from_store(self, schema_keyname: str, params: dict) -> List[dict]:
        if schema_keyname not in self._stores:
            raise NotFound("not-found-table", f"Not found schema store '{schema_keyname}'")
        if not params:
            return list(self._stores[schema_keyname].values())
        res = []
        for item in self._stores[schema_keyname].values():
            if all(item.get(k) == v for k, v in params.items()):
                res.append(item)
        return res

    def insert_data_into_store(self, schema_keyname: str, data: dict) -> Hashable:
        uid = str(uuid.uuid4())
        data["uid"] = uid
        self._stores[schema_keyname][uid] = data
        return uid

    def update_data_in_store(self, schema_keyname: str, data: dict,
                             uid_data: Hashable) -> Optional[Hashable]:
        item = self._stores.get(schema_keyname, {}).get(uid_data)
        if "uid" in data:
            del data["uid"]
        if not item:
            return None
        item.update(data)
        return uid_data

    def delete_data_from_store(self, schema_keyname: str, uid_data: Hashable) -> Optional[Hashable]:
        res = self._stores[schema_keyname].pop(uid_data)
        return uid_data if res else None
