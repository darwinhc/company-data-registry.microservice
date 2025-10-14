from bisslog.utils.mapping import Mapper
from src.infra.entry_points.setup import setup
from src.domain.use_cases.schema.change_current_schema_def_version import CHANGE_CURRENT_SCHEMA_DEF_VERSION


setup()
mapper_http_0 = Mapper("mapper_http_0", {"path_query.schema_keyname": "schema_keyname", "body.uid_schema_version": "uid_schema_version"})
mapper_http = Mapper("mapper_http", {
    "event.payload": "body",
    "event.queryStringParameters": "params",
    "event.pathParameters": "path_query",
    "event.headers": "headers",
})


def lambda_handler(event, context):
    if "httpMethod" in event:
        mapped_standard_request = mapper_http.map({"event": event, "context": context})
        # if event.get("resource", "").endswith("/schemas/{schema_keyname}/version") and event.get("httpMethod") == "PUT":
        request_to_uc : dict = mapper_http_0.map(mapped_standard_request)
        uc_response = CHANGE_CURRENT_SCHEMA_DEF_VERSION(**request_to_uc)
        return {"statusCode": 200, "body": uc_response}
    raise RuntimeError(
        f"Unrecognized event format. No matching handler found for the incoming event: {str(event)[:500]}"
    )
