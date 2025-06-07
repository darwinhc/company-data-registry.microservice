from bisslog import bisslog_db as db

from ..database.implementations.vanilla_cache.schema_def_version_vanilla_cache_div import \
    SchemaDefVersionVanillaCacheDiv
from ..database.implementations.vanilla_cache.schema_vanilla_cache_division import \
    SchemaVanillaCacheDivision
from ..database.implementations.vanilla_cache.stores_vanilla_cache_division import \
    StoresVanillaCacheDivision


def setup():
    db.register_adapters(stores=StoresVanillaCacheDivision(), schema=SchemaVanillaCacheDivision(),
                         schema_version=SchemaDefVersionVanillaCacheDiv())
