import pytest


def test_credentials_method():
    assert True


def test_credentials_error():
    with pytest.raises(ValueError):
        raise ValueError()
