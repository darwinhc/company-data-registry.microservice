from bisslog import use_case, bisslog_db as db

@use_case
def delete_all_inactive_schema_versions(*_, **kwargs) -> dict:
    """Use case for deleting all inactive schema versions.

    Parameters
    ----------
    **kwargs
        Keyword arguments for the use case.

    Returns
    -------
    dict
        A dictionary containing the result of the use case.
    """

    schemas = db.schema.get_schemas()
    days = kwargs.get('days', 60)
    res = {}
    for schema in schemas:
        res_by_schema = db.schema_version.delete_inactive_schema_versions(
            schema_keyname=schema.schema_keyname,
            current_version=schema.current_version,
            days=days
        )
        res[schema.schema_keyname] = res_by_schema

    return {"result": res}
