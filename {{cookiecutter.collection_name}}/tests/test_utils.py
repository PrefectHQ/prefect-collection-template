import pytest

from {{ cookiecutter.collection_name }}.utils import (
    camel_to_snake_case,
    initialize_return_fields_defaults,
    strip_kwargs
)


@pytest.mark.parametrize("string", ["someIDString", "SomeIDString", "some_id_string"])
def test_camel_to_snake_case(string):
    assert camel_to_snake_case(string) == "some_id_string"


def test_initialize_return_fields_defaults():
    return_fields_defaults = initialize_return_fields_defaults("test_config.json")
    assert return_fields_defaults == {
        ("categories",): ["total"],
        ("categories", "category"): ["title", "alias"]
    }


def test_strip_kwargs():
    assert strip_kwargs({"a": None, "b": None}) == {}
    assert strip_kwargs({"a": "", "b": None}) == {"a": ""}
    assert strip_kwargs({"a": "abc", "b": "def"}) == {"a": "abc", "b": "def"}
    assert strip_kwargs(**{"a": "abc", "b": "def"}) == {"a": "abc", "b": "def"}
    assert strip_kwargs(dict(a=[])) == {"a": []}
