from unittest.mock import MagicMock

import httpx
import pytest
from prefect import flow

from {{cookiecutter.collection_slug}}.rest import HTTPMethod, execute_endpoint


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


@pytest.mark.parametrize("http_method", ["get", HTTPMethod.GET])
async def test_execute_endpoint(http_method):
    url = "https://prefect.io/"
    params = dict(a="A", b="B")

    @flow
    async def test_flow():
        credentials = MockCredentials()
        result = await execute_endpoint(
            url, credentials, http_method=http_method, params=params
        )
        return result

    assert (await test_flow()) == {"url": url, "params": params}


@pytest.mark.parametrize("responses", [{}, {404: "Testing message"}, None])
async def test_execute_endpoint_error(responses):
    url = "BAD URL"

    @flow
    async def test_flow():
        credentials = MockCredentials()
        result = await execute_endpoint(
            url, credentials, http_method="get", responses=responses
        )
        return result

    if not responses:
        with pytest.raises(httpx.HTTPStatusError, match="Not found"):
            (await test_flow())
    else:
        with pytest.raises(httpx.HTTPStatusError, match="Testing message"):
            (await test_flow())
