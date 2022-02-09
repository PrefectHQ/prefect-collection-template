from prefect import task

@task
def hello_prefect_collection():
    return "Hello, prefect-collection!"


@task
def goodbye_prefect_collection():
    return "Goodbye, prefect-collection!"

