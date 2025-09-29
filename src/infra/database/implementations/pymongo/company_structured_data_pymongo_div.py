from typing import List

from bisslog_pymongo import bisslog_exc_mapper_pymongo, BasicPymongoHelper
from src.infra.database.company_structured_data_division import CompanyStructuredDataDivision


class CompanyStructuredDataMongoDivision(CompanyStructuredDataDivision, BasicPymongoHelper):
    """
    Concrete implementation of CompanyStructuredDataDivision using PyMongo.
    """

    col = "company_structured_data"

    @bisslog_exc_mapper_pymongo
    def get_company_structured_data(self, id_data: str) -> dict:
        query = {"_id": str(id_data)}
        return self.find_one(self.col, query, selection={})

    @bisslog_exc_mapper_pymongo
    def update_company_structured_data(self, company_id: str, data: dict) -> bool:
        query = {"_id": self.verify_query({"_id": str(company_id)})["_id"]}
        update = {"$set": data}
        result = self.get_collection(self.col).update_one(query, update)
        return result.modified_count == 1

    @bisslog_exc_mapper_pymongo
    def delete_company_structured_data(self, company_id: str) -> bool:
        query = {"_id": self.verify_query({"_id": str(company_id)})["_id"]}
        result = self.get_collection(self.col).delete_one(query)
        return result.deleted_count == 1

    @bisslog_exc_mapper_pymongo
    def list_all_companies_structured_data(self) -> List[dict]:
        cursor = self.get_collection(self.col).find({})
        return self.stringify_list_identifier(cursor)

    @bisslog_exc_mapper_pymongo
    def create_company_structured_data(self, data: dict) -> str:
        return self.insert_one(self.col, data)
