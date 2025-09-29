from bisslog.utils.mapping import Mapper
from src.infra.entry_points.setup import setup
from src.domain.use_cases.company_data.insert_company_data import INSERT_COMPANY_DATA


setup()
mapper_http_0 = Mapper("mapper_http_0", {"path_query.schema_keyname": "schema_keyname", "body": "data"})
mapper_http = Mapper("mapper_http", {
    "event.payload": "body",
    "event.queryStringParameters": "params",
    "event.pathParameters": "path_query",
    "event.headers": "headers",
})
mapper_consumer_sqs = Mapper("mapper_consumer_sqs", {"body": "event"})
mapper_consumer_sqs_0 = Mapper("mapper_consumer_sqs_0", {"event.schema_keyname": "schema_keyname", "event.body": "data"})
mapper_consumer_sns = Mapper("mapper_consumer_sns", {"Message": "event"})
mapper_consumer_sns_0 = Mapper("mapper_consumer_sns_0", {"event.schema_keyname": "schema_keyname", "event.body": "data"})
mapper_consumer_event_bridge = Mapper("mapper_consumer_event_bridge", {"detail": "event"})
mapper_consumer_event_bridge_0 = Mapper("mapper_consumer_event_bridge_0", {"event.schema_keyname": "schema_keyname", "event.body": "data"})


def lambda_handler(event, context):
    if "httpMethod" in event:
        mapped_standard_request = mapper_http.map({"event": event, "context": context})
        # if event.get("resource", "").endswith("/company/data/{schema_keyname}") and event.get("httpMethod") == "POST":
        request_to_uc : dict = mapper_http_0.map(mapped_standard_request)
        uc_response = INSERT_COMPANY_DATA(**request_to_uc)
        return {"statusCode": 200, "body": uc_response}
    if event.get("Records") and event["Records"][0].get("eventSource") == "aws:sqs":
        response = []
        for record in event["Records"]:
            mapped_standard_event_sqs = mapper_consumer_sqs.map(record)
            # queue_arn = record.get("eventSourceARN", "")
            # if "company_data_insertion.queue" in queue_arn:
            request_to_uc : dict = mapper_consumer_sqs_0.map(mapped_standard_event_sqs)
            uc_response = INSERT_COMPANY_DATA(**request_to_uc)
            response.append(uc_response)
            return {"statusCode": 200, "body": response}
    if event.get("Records") and event["Records"][0].get("EventSource") == "aws:sns":
        response = []
        for record in event["Records"]:
            mapped_standard_event_sns = mapper_consumer_sns.map(record['Sns'])
            # queue_arn = record.get("EventSubscriptionArn", "")
            # if "company_data_insertion.queue" in queue_arn:
            request_to_uc : dict = mapper_consumer_sns_0.map(mapped_standard_event_sns)
            uc_response = INSERT_COMPANY_DATA(**request_to_uc)
            response.append(uc_response)
            return {"statusCode": 200, "body": response}
    if event.get("source") or event.get("detail-type") or event.get("version") == "0":
        response = []
        mapped_standard_event = mapper_consumer_event_bridge.map(event)
        # if "company_data_insertion.queue" in event.get("source", ""):
        request_to_uc : dict = mapper_consumer_event_bridge_0.map(mapped_standard_event)
        uc_response = INSERT_COMPANY_DATA(**request_to_uc)
        response.append(uc_response)
        return {"statusCode": 200, "body": response}
    raise RuntimeError(
        f"Unrecognized event format. No matching handler found for the incoming event: {str(event)[:500]}"
    )
