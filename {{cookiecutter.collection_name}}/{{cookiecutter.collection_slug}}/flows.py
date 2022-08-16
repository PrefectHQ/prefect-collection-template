"""This is an example flows module"""
from prefect import flow

from {{ cookiecutter.collection_slug }}.tasks import (
    goodbye_{{ cookiecutter.collection_slug }},
    hello_{{ cookiecutter.collection_slug }},
)
from {{ cookiecutter.collection_slug }}.blocks import {{ cookiecutter.collection_name.split('-')[1:] | join | title}}Block


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    {{ cookiecutter.collection_name.split('-')[1:] | join | title}}Block().seed_value_for_example()
    block = {{ cookiecutter.collection_name.split('-')[1:] | join | title}}Block.load("sample-block")

    print(hello_{{ cookiecutter.collection_slug }}())
    print(f"The block's value: {block.value}")
    print(goodbye_{{ cookiecutter.collection_slug }}())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
