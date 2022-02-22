from prefect import flow

from {{ cookiecutter.collection_slug }}.tasks import (
    goodbye_{{ cookiecutter.collection_slug }},
    hello_{{ cookiecutter.collection_slug }},
)


def test_hello_{{ cookiecutter.collection_slug }}():
    @flow
    def test_flow():
        return hello_{{ cookiecutter.collection_slug }}()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, {{ cookiecutter.collection_name }}!"


def goodbye_hello_{{ cookiecutter.collection_slug }}():
    @flow
    def test_flow():
        return goodbye_{{ cookiecutter.collection_slug }}()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, {{ cookiecutter.collection_name }}!"
