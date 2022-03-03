"""This is an example flows module"""
from prefect import flow

from {{ cookiecutter.collection_slug }}.tasks import (
    goodbye_{{ cookiecutter.collection_slug }},
    hello_{{ cookiecutter.collection_slug }},
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    print(hello_{{ cookiecutter.collection_slug }})
    print(goodbye_{{ cookiecutter.collection_slug }})
