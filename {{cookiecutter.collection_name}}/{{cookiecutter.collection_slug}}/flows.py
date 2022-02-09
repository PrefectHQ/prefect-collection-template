from prefect import flow
from {{ cookiecutter.collection_slug }}.tasks import hello_{{ cookiecutter.collection_slug }}, goodbye_{{ cookiecutter.collection_slug }}

@flow
def hello_and_goodbye():
    print(hello_{{ cookiecutter.collection_slug }})
    print(goodbye_{{ cookiecutter.collection_slug }})
