from prefect import flow
from prefect_collection.tasks import hello_prefect_collection, goodbye_prefect_collection

def test_hello_prefect_collection():
    @flow
    def test_flow():
        return hello_prefect_collection()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Hello, prefect-collection!"


def goodbye_hello_prefect_collection():
    @flow
    def test_flow():
        return goodbye_prefect_collection()

    flow_state = test_flow()
    task_state = flow_state.result()
    assert task_state.result() == "Goodbye, prefect-collection!"