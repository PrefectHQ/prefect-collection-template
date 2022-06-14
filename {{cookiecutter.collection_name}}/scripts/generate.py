from cookiecutter.main import cookiecutter
from prefect_collection_generator.rest import populate_collection_repo


# UPDATE THIS SECTION
extra_context = {
    "collection_name": "{{ cookiecutter.collection_name }}",
    "collection_short_description": "Prefect integrations interacting with {{ cookiecutter.collection_name }}",
}
collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
service_name = "{{ cookiecutter.collection_name }}"
urls = [

]
routes = None
overwrite = True

cookiecutter(
    collection_template_url,
    no_input=True,
    checkout="generated_rest",
    extra_context=extra_context,
    overwrite_if_exists=True
)

populate_collection_repo(
    service_name,
    urls,
    routes=routes,
    overwrite=overwrite,
)
