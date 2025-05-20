from collections.abc import Hashable

from bisslog import bisslog_db as db, use_case
from bisslog.exceptions.domain_exception import NotFound


@use_case
def delete_data_company(schema_keyname: str, uid_data: Hashable):
    """Execute the use case to delete company data.

    Parameters
    ----------
    schema_keyname : str
        The keyname of the schema to delete.
    uid_data : Hashable
        The unique identifier of the data to delete.

    Returns
    -------
    None
        This method does not return any value.
    """
    uid_data = db.stores.delete_data_from_store(schema_keyname, uid_data)
    if uid_data is None:
        raise NotFound("data-not-found",
                       f"Data with (uid) {uid_data} not found in schema {schema_keyname}.")
    return {"deleted": uid_data}
