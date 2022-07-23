from {{ cookiecutter.collection_slug }}.flows import hello_and_goodbye


def test_hello_and_goodbye_flow():
    result = hello_and_goodbye()
    assert result == "Done"
