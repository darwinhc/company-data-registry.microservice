import pytest
from src.domain.model.schema import Schema


def test_valid_schema_instance():
    """
    Test creating a Schema instance with valid attributes.

    Returns
    -------
    None
    """
    schema = Schema(
        schema_name="CompanyConfig",
        schema_keyname="company_services",
        schema_identifier="service_id",
        current_schema_definition={
            "type": "object",
            "properties": {
                "service": {"type": "string"}
            },
            "required": ["service"]
        }
    )
    assert isinstance(schema, Schema)


@pytest.mark.parametrize("field_name, value", [
    ("schema_keyname", None),
    ("schema_keyname", 123),
    ("schema_keyname", "1invalid"),
    ("schema_keyname", "in"),
    ("schema_keyname", "a" * 51),
    ("schema_identifier", ""),
    ("schema_identifier", "has spaces"),
    ("schema_identifier", "!@#"),
])
def test_invalid_str_identifier(field_name, value):
    """
    Test invalid identifier strings for `schema_keyname` and `schema_identifier`.

    Parameters
    ----------
    field_name : str
        The name of the field being tested.
    value : Any
        The invalid value to assign to the field.

    Returns
    -------
    None
    """
    valid_kwargs = {"schema_name": "CompanyConfig", "schema_keyname": "valid_key",
                    "schema_identifier": "valid_id",
                    "schema_definition": {"type": "object"}, field_name: value}
    with pytest.raises(ValueError, match=field_name):
        Schema(**valid_kwargs)


@pytest.mark.parametrize("name", [
    None,
    123,
    "ab",
    "a" * 101,
])
def test_invalid_schema_name(name):
    """
    Test invalid `schema_name` values that should raise ValueError.

    Parameters
    ----------
    name : Any
        The invalid name to use.

    Returns
    -------
    None
    """
    with pytest.raises(ValueError, match="schema_name"):
        Schema(
            schema_name=name,
            schema_keyname="valid_key",
            schema_identifier="valid_id",
            current_schema_definition={"type": "object"}
        )


def test_schema_definition_not_dict():
    """
    Test that a non-dictionary `schema_definition` raises ValueError.

    Returns
    -------
    None
    """
    with pytest.raises(ValueError, match="must be a dictionary"):
        Schema(
            schema_name="CompanyConfig",
            schema_keyname="key",
            schema_identifier="identifier",
            current_schema_definition="not_a_dict"
        )


def test_schema_definition_invalid_structure():
    """
    Test that an invalid JSON Schema structure raises an exception.

    Returns
    -------
    None
    """
    invalid_schema = {
        "type": "object",
        "properties": {
            "field": {"type": "nonexistent_type"}
        }
    }
    with pytest.raises(Exception):
        Schema(
            schema_name="CompanyConfig",
            schema_keyname="key",
            schema_identifier="identifier",
            current_schema_definition=invalid_schema
        )
