"""
Used for generating the repository from scratch.
"""
from pathlib import Path

from prefect_collection_generator.gql import populate_collection_repo

THIS_DIRECTORY = Path(__file__).parent.absolute()
REPO_DIRECTORY = THIS_DIRECTORY.parent

# # USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
# from cookiecutter.main import cookiecutter

# extra_context = {
#     "full_name":  "Prefect Technologies, Inc.",
#     "email": "help@prefect.io",
#     "github_organization": "PrefectHQ",
#     "collection_name": "prefect-github",
#     "collection_short_description": "Prefect integrations interacting with GitHub",  # noqa
# }

# collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_graphql",
#     extra_context=extra_context,
#     overwrite_if_exists=True
# )
# REPO_DIRECTORY = THIS_DIRECTORY / "prefect_github"  # redirects repo_directory

# UPDATE THESE AS DESIRED
service_name = ""  # e.g. GitHub
service_url = ""  # e.g. https://api.github.com/graphql
token_path = Path(f"~/.secrets/{service_name.lower()}").expanduser()
with open(token_path) as f:
    token = f.read().strip()  # e.g. ghp_...
root_to_op_types = {
    # if None, generates all available op_types
    "query": None,  # e.g. ["repository", "pull_requests"]
    "mutation": None,  # e.g. ["add_star", "remove_star"]
}
overwrite = True
repo_directory = "../"

populate_collection_repo(
    service_name,
    service_url,
    token,
    root_to_op_types,
    repo_directory=REPO_DIRECTORY,
    overwrite=overwrite
)
