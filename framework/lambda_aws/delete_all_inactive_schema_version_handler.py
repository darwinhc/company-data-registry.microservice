from bisslog.utils.mapping import Mapper
from src.infra.entry_points.setup import setup
from src.domain.use_cases.schema.delete_all_inactive_schema_version import delete_all_inactive_schema_versions


setup()
mapper_schedule_event_bridge = Mapper("mapper_schedule_event_bridge", {"detail": "event"})


def lambda_handler(event, context):
    if event.get("source") == "aws.events" and event.get("detail-type") == "Scheduled Event":
        response = []
        request_to_uc = mapper_schedule_event_bridge.map(event)
        uc_response = delete_all_inactive_schema_versions(**request_to_uc)
        response.append(uc_response)
        return {"statusCode": 200, "body": response}
    raise RuntimeError(
        f"Unrecognized event format. No matching handler found for the incoming event: {str(event)[:500]}"
    )
