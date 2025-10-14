from bisslog.utils.mapping import Mapper
from src.infra.entry_points.setup import setup
from src.domain.use_cases.company_data.get_company_data import GetCompanyData


setup()
GET_COMPANY_DATA = GetCompanyData()
mapper_http_0 = Mapper("mapper_http_0", {"path_query.schema_keyname": "schema_keyname", "params": "params"})
mapper_http = Mapper("mapper_http", {
    "event.queryStringParameters": "params",
    "event.pathParameters": "path_query",
})


def lambda_handler(event, context):
    if "httpMethod" in event:
        mapped_standard_request = mapper_http.map({"event": event, "context": context})
        if event.get("resource", "").endswith("/company/data/{schema_keyname}") and event.get("httpMethod") == "GET":
            request_to_uc : dict = mapper_http_0.map(mapped_standard_request)
            uc_response = GET_COMPANY_DATA(**request_to_uc)
            return {"statusCode": 200, "body": uc_response}
        if event.get("resource", "").endswith("/company-data/{schema_keyname}") and event.get("httpMethod") == "GET":
            request_to_uc = mapped_standard_request
            request_to_uc.update(mapped_standard_request.get("params"))
            request_to_uc.update(mapped_standard_request.get("path_query"))
            uc_response = GET_COMPANY_DATA(**request_to_uc)
            return {"statusCode": 200, "body": uc_response}
    raise RuntimeError(
        f"Unrecognized event format. No matching handler found for the incoming event: {str(event)[:500]}"
    )
