"""Implementation of SchemaDefVersionDivision using PyMongo."""

from collections.abc import Hashable
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from typing import Optional, List

from bisslog_pymongo import BasicPymongoHelper, bisslog_exc_mapper_pymongo

from src.domain.model.schema_definition_version import SchemaDefinitionVersion
from src.infra.database.schema_def_version_division import SchemaDefVersionDivision


class SchemaDefVersionMongoDivision(SchemaDefVersionDivision, BasicPymongoHelper):
    """Concrete implementation of SchemaDefVersionDivision using PyMongo."""

    col = "schema_def_versions"

    @bisslog_exc_mapper_pymongo
    def create_schema_version(self, schema_version: SchemaDefinitionVersion) -> Hashable:
        data = asdict(schema_version)
        return self.insert_one(self.col, data)

    @bisslog_exc_mapper_pymongo
    def get_schema_version(self, uid: Hashable) -> Optional[SchemaDefinitionVersion]:
        res = self.find_one(self.col, {"_id": str(uid)}, selection={})
        if res is None:
            return None
        res = self.stringify_identifier(res)
        return SchemaDefinitionVersion(**res)

    @bisslog_exc_mapper_pymongo
    def get_schema_versions(self, schema_keyname: str) -> List[SchemaDefinitionVersion]:
        query = {"schema_keyname": schema_keyname}
        cursor = self.get_collection(self.col).find(query)
        return [SchemaDefinitionVersion(**x) for x in self.stringify_list_identifier(cursor)]

    @bisslog_exc_mapper_pymongo
    def delete_schema_version(self, uid: Hashable) -> Optional[Hashable]:
        query = {"_id": self.verify_query({"_id": str(uid)})["_id"]}
        res = self.get_collection(self.col).delete_one(query)
        if res.deleted_count == 1:
            return str(uid)
        return None

    @bisslog_exc_mapper_pymongo
    def delete_inactive_schema_versions(self, schema_keyname: str,
                                        current_version: Hashable, days: int) -> List[Hashable]:
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
        query = {
            "schema_keyname": schema_keyname,
            "_id": {"$ne": self.verify_query({"_id": str(current_version)})["_id"]},
            "created_at": {"$lt": cutoff_date}
        }
        deleted_ids = [str(doc["_id"]) for doc in
                       self.get_collection(self.col).find(query, {"_id": 1})]
        self.get_collection(self.col).delete_many(query)
        return deleted_ids
