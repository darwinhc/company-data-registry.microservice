from typing import List, Dict
from bisslog import bisslog_db as db

from src.domain.use_cases.company_data.get_company_data import GetCompanyData
from src.domain.use_cases.company_data.insert_company_data import INSERT_COMPANY_DATA
from src.domain.use_cases.schema.create_schema import CREATE_SCHEMA
from src.infra.database.implementations.vanilla_cache.schema_def_version_vanilla_cache_div import \
    SchemaDefVersionVanillaCacheDiv
from src.infra.database.implementations.vanilla_cache.schema_vanilla_cache_division import \
    SchemaVanillaCacheDivision
from src.infra.database.implementations.vanilla_cache.stores_vanilla_cache_division import \
    StoresVanillaCacheDivision
from tests.integration.vanilla.constants import LANGUAGE_SCHEMA

GET_COMPANY_DATA = GetCompanyData()

db.register_adapters(schema=SchemaVanillaCacheDivision(),
                     stores=StoresVanillaCacheDivision(),
                     schema_def_version=SchemaDefVersionVanillaCacheDiv())

def test_complete_process():
    """
    Test the complete process of the application.
    """


    # Step 1: Create schema
    data_schema = {
        "schema_keyname": "language", "schema_name": "Language",
        "schema_description": "Language schema", "current_schema_definition": LANGUAGE_SCHEMA,
    }
    res1 = CREATE_SCHEMA(schema_info=data_schema)
    schema = res1["schema"]

    # Step 2: Insert data
    data1 = {"code": "es", "name": "español", "emoji": "🇪🇸",
             "translations": {"en": "Spanish", "fr": "Espagnol", "de": "Spanisch"}}
    uid_spanish = INSERT_COMPANY_DATA("language", data1)
    data2 = {"code": "en", "name": "english", "emoji": "🇬🇧",
             "translations": {"es": "inglés", "fr": "anglais", "de": "Englisch", "it": "inglese",
                              "pt": "inglês", "zh": "英语", "ja": "英語", "ru": "английский"}}
    uid_english = INSERT_COMPANY_DATA("language", data2)

    all_languages = GET_COMPANY_DATA("language")
    all_languages["data"] : List[Dict]
    assert 2 == len(all_languages["data"])
    assert all_languages

