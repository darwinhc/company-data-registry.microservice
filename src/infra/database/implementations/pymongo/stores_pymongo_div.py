"""Stores division for PyMongo implementation."""
from collections.abc import Hashable
from typing import Optional, List

from bisslog_pymongo import BasicPymongoHelper, bisslog_exc_mapper_pymongo

from src.domain.model.schema import Schema
from src.infra.database.stores_division import StoresDivision


class StoreMongoDivision(StoresDivision, BasicPymongoHelper):
    """Concrete implementation of StoresDivision using PyMongo."""

    @bisslog_exc_mapper_pymongo
    def create_store_of_schema(self, schema: Schema) -> bool:
        """Create a new store for the schema in the database."""
        self.database.create_collection(schema.schema_keyname)
        return True

    @bisslog_exc_mapper_pymongo
    def alter_store_of_schema(self, schema: Schema) -> bool:
        return True

    @bisslog_exc_mapper_pymongo
    def get_one_data_from_store(self, schema_keyname: str, uid_data: Hashable) -> Optional[dict]:
        res = self.get_collection(schema_keyname).find_one({"_id": uid_data})
        return self.stringify_identifier(res)

    @bisslog_exc_mapper_pymongo
    def get_data_from_store(self, schema_keyname: str, params: dict) -> List[dict]:
        res = self.get_collection(schema_keyname).find(params)
        if res is None:
            return []
        return self.stringify_list_identifier(res)

    @bisslog_exc_mapper_pymongo
    def insert_data_into_store(self, schema_keyname: str, data: dict) -> Optional[Hashable]:
        res = self.get_collection(schema_keyname).insert_one(data)
        return str(res.inserted_id)

    @bisslog_exc_mapper_pymongo
    def update_data_in_store(self, schema_keyname: str, data: dict,
                             uid_data: Hashable) -> Optional[Hashable]:
        res = self.get_collection(schema_keyname).update_one(
            {"_id": uid_data}, {"$set": data}
        )
        if res.modified_count == 1:
            return uid_data
        return None

    @bisslog_exc_mapper_pymongo
    def delete_data_from_store(self, schema_keyname: str, uid_data: Hashable) -> Optional[Hashable]:
        res = self.get_collection(schema_keyname).delete_one({"_id": uid_data})
        if res.deleted_count == 1:
            return uid_data
        return None
