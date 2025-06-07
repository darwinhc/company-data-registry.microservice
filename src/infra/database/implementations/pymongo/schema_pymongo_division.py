from dataclasses import asdict
from typing import Hashable, Optional, List

from bisslog_pymongo import BasicPymongoHelper, bisslog_exc_mapper_pymongo

from src.domain.model.schema import Schema
from src.domain.model.schema_base import SchemaBase
from src.infra.database.schema_division import SchemaDivision


class SchemaMongoDivision(SchemaDivision, BasicPymongoHelper):

    col = "schemas"

    @bisslog_exc_mapper_pymongo
    def get_schema(self, schema_keyname: str) -> Optional[Schema]:
        res = self.get_collection(self.col).find_one({"schema_keyname": schema_keyname})
        return self.stringify_identifier(res)

    @bisslog_exc_mapper_pymongo
    def get_schemas(self, params: dict) -> List[Schema]:
        res = self.get_collection(self.col).find(params)
        return self.stringify_list_identifier(res)

    @bisslog_exc_mapper_pymongo
    def create_schema(self, schema: Schema) -> Hashable:
        res = self.get_collection(self.col).insert_one(asdict(schema))
        return res.inserted_id

    @bisslog_exc_mapper_pymongo
    def delete_schema(self, schema_keyname: str) -> Optional[Hashable]:
        res = self.get_schema(schema_keyname)
        if not res:
            return None
        res = (self.get_collection(self.col)
               .delete_one({"schema_keyname": schema_keyname}))
        if res.deleted_count == 1:
            return res["_id"]
        return None

    @bisslog_exc_mapper_pymongo
    def update_schema(self, schema: SchemaBase) -> Optional[Hashable]:
        res = self.get_collection(self.col).update_one(
            {"schema_keyname": schema.schema_keyname},
            {"$set": asdict(schema)}
        )
        if res.modified_count == 1:
            return res.upserted_id
        return None

    @bisslog_exc_mapper_pymongo
    def update_schema_definition(self, schema_keyname: str, new_version: Hashable,
                                 definition: dict) -> Optional[Hashable]:
        res = self.get_collection(self.col).update_one(
            {"schema_keyname": schema_keyname},
            {"$set": {"current_version": new_version,
                      "current_schema_definition": definition}}
        )
        if res.modified_count == 1:
            return res.upserted_id
        return None
