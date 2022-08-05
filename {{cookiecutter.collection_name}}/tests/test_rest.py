from unittest.mock import MagicMock

import httpx
import pytest
from prefect import flow

from {{cookiecutter.collection_slug}}.rest import HTTPMethod, execute_endpoint, strip_kwargs


class MockAsyncClient:
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return self

    def raise_404(self):
        raise httpx.HTTPStatusError(
            "Not found",
            request=httpx.Request("get", "url"),
            response=httpx.Response(404),
        )

    def raise_not(self):
        pass

    async def get(self, url, params):
        raise_for_status = self.raise_404 if url == "BAD URL" else self.raise_not
        return MagicMock(
            json=lambda: {"url": url, "params": params},
            raise_for_status=raise_for_status,
            status_code=404,
        )


class MockCredentials(MagicMock):
    def get_client(self):
        return MockAsyncClient()


@pytest.mark.parametrize("params", [dict(a="A", b="B"), None])
@pytest.mark.parametrize("http_method", ["get", HTTPMethod.GET])
async def test_execute_endpoint(params, http_method):
    url = "https://prefect.io/"

    @flow
    async def test_flow():
        credentials = MockCredentials()
        response = await execute_endpoint(
            url, credentials, http_method=http_method, params=params
        )
        result = response.json()
        return result

    assert (await test_flow()) == {"url": url, "params": params}


def test_strip_kwargs():
    assert strip_kwargs(**{"a": None, "b": None}) == {}
    assert strip_kwargs(**{"a": "", "b": None}) == {"a": ""}
    assert strip_kwargs(**{"a": "abc", "b": "def"}) == {"a": "abc", "b": "def"}
    assert strip_kwargs(a="abc", b="def") == {"a": "abc", "b": "def"}
    assert strip_kwargs(**dict(a=[])) == {"a": []}
