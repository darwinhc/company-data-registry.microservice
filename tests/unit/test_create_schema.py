import pytest
from unittest.mock import patch
from src.domain.use_cases.schema.create_schema import CreateSchema
from src.domain.model.schema import Schema
from bisslog.exceptions.external_interactions_errors import ExternalInteractionError


@pytest.fixture
def schema_info():
    """Provides valid schema input data."""
    return {
        "schema_name": "Valid Name",
        "schema_keyname": "valid_schema",
        "schema_identifier": "valid_identifier",
        "schema_definition": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"}
            },
            "required": ["name"]
        }
    }


@pytest.fixture
def user_info():
    """Provides dummy user info."""
    return {
        "user_id": "test_user"
    }


@pytest.fixture
def use_case():
    """Initializes the CreateSchema use case with a mocked logger."""
    uc = CreateSchema()
    return uc


@patch("src.domain.use_cases.create_schema.db")
def test_successful_schema_creation(mock_db, use_case, schema_info, user_info):
    """Should return a Schema instance when all steps succeed."""
    mock_db.schema.create_schema.return_value = "uid-001"
    mock_db.schema.create_store_of_schema.return_value = None

    result = use_case(schema_info, user_info)

    assert isinstance(result, Schema)
    assert result.schema_keyname == "valid_schema"
    mock_db.schema.create_schema.assert_called_once()
    mock_db.schema.create_store_of_schema.assert_called_once()


@patch("src.domain.use_cases.create_schema.db")
def test_error_on_create_schema_raises(mock_db, use_case, schema_info, user_info, caplog):
    """Should raise ExternalInteractionError if schema creation fails."""
    mock_db.schema.create_schema.side_effect = ExternalInteractionError("Creation failed")

    with caplog.at_level("ERROR"):
        with pytest.raises(ExternalInteractionError):
            use_case(schema_info, user_info)

    mock_db.schema.create_schema.assert_called_once()
    error_logs = [r for r in caplog.records if r.levelname == "ERROR"]
    assert any("There was an error creating the schema: " in r.message for r in error_logs)


@patch("src.domain.use_cases.create_schema.db")
def test_error_on_create_store_triggers_rollback(mock_db, use_case, schema_info, user_info, caplog):
    """Should delete schema and raise error if store creation fails."""
    mock_db.schema.create_schema.return_value = "uid-002"
    mock_db.schema.create_store_of_schema.side_effect = ExternalInteractionError("Store failed")

    with caplog.at_level("INFO"):
        with pytest.raises(ExternalInteractionError):
            use_case(schema_info, user_info)

    mock_db.schema.create_schema.assert_called_once()
    mock_db.schema.create_store_of_schema.assert_called_once()
    mock_db.schema.delete_schema.assert_called_once_with("valid_schema")

    info_logs = [r for r in caplog.records if r.levelname == "INFO"]
    error_logs = [r for r in caplog.records if r.levelname == "ERROR"]

    assert any("Schema was successfully deleted as a rollback" in r.message for r in info_logs)
    assert any("Schema was not successfully created: " in r.message for r in error_logs)
