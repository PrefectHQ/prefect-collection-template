from prefect import task

@task
def hello_{{ cookiecutter.collection_slug }}():
    return "Hello, {{ cookiecutter.collection_name }}!"


@task
def goodbye_{{ cookiecutter.collection_slug }}():
    return "Goodbye, {{ cookiecutter.collection_name }}!"

