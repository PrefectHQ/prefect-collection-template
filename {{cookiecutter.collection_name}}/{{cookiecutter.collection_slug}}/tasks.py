"""This is an example tasks module"""
from prefect import task


@task
def hello_{{ cookiecutter.collection_slug }}() -> str:
    """
    Sample task that says hello!

    Returns:
        A greeting for your collection
    """
    return "Hello, {{ cookiecutter.collection_name }}!"


@task
def goodbye_{{ cookiecutter.collection_slug }}() -> str:
    """
    Sample task that says goodbye!

    Returns:
        A farewell for your collection
    """
    return "Goodbye, {{ cookiecutter.collection_name }}!"
