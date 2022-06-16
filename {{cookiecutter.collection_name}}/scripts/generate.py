"""
Used for generating the repository from scratch.
"""
# from cookiecutter.main import cookiecutter
from prefect_collection_generator.gql import populate_collection_repo


# USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
# extra_context = {
#     "full_name":  "{{ cookiecutter.full_name }}",  # e.g. "Prefect Technologies, Inc.",
#     "email": "{{ cookiecutter.email }}",  # e.g. "help@prefect.io",
#     "github_organization": "{{ cookiecutter.github_organization }}",  # e.g. "PrefectHQ",
#     "collection_name": "{{ cookiecutter.collection_name }}",
#     "collection_short_description": "Prefect integrations interacting with {{ cookiecutter.collection_name }}",
# }

# collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_rest",
#     extra_context=extra_context,
#     overwrite_if_exists=True
# )

# UPDATE THESE AS DESIRED
service_name = ""  # e.g. GitHub
service_url = ""  # e.g. https://api.github.com/graphql
token = ""  # e.g. ghp_...
root_to_op_types = {
    "query": None,  # e.g. ["repository", "pull_requests"]
    "mutation": None,  # e.g. ["add_star", "remove_star"]
}
overwrite = True

populate_collection_repo(
    service_name,
    service_url,
    token,
    root_to_op_types,
)
