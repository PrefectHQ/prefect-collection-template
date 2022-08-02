"""
Used for appending extra routes after initial generation.
"""
from pathlib import Path

# from cookiecutter.main import cookiecutter

from prefect_collection_generator.rest import RESTGenerator

THIS_DIRECTORY = Path(__file__).parent.absolute()
REPO_DIRECTORY = THIS_DIRECTORY.parent

# USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
# extra_context = {
#     "full_name":  "{{ cookiecutter.full_name }}",  # e.g. "Prefect Technologies, Inc.",
#     "email": "{{ cookiecutter.email }}",  # e.g. "help@prefect.io",
#     "github_organization": "{{ cookiecutter.github_organization }}",  # e.g. "PrefectHQ",
#     "collection_name": "{{ cookiecutter.collection_name }}",
#     "collection_short_description": "Prefect integrations interacting with {{ cookiecutter.collection_name }}",  # noqa
# }

# collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_rest",
#     extra_context=extra_context,
#     overwrite_if_exists=True
# )
# REPO_DIRECTORY = THIS_DIRECTORY / "prefect_github"  # redirects repo_directory

# UPDATE THIS SECTION
service_name = "{{ cookiecutter.collection_name }}"
base_directory = REPO_DIRECTORY / "{{ cookiecutter.collection_name }}"
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
