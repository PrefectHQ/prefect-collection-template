"""
Used for appending extra routes after initial generation.
"""
from prefect_collection_generator.rest import RESTGenerator

# UPDATE THIS SECTION
service_name = "{{ cookiecutter.collection_name }}"
base_directory = "../{{ cookiecutter.collection_name }}"
overwrite = False
url = ""
routes = []

rest_generator = RESTGenerator(
    service_name,
    base_directory=base_directory,
    overwrite=overwrite
)
rest_generator.generate_endpoint_files(url, routes=routes)
rest_generator.generate_docs_files()
