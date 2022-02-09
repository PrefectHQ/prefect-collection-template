from prefect import flow
from prefect_collection.tasks import hello_prefect_collection, goodbye_prefect_collection

@flow
def hello_and_goodbye():
    print(hello_prefect_collection)
    print(goodbye_prefect_collection)
