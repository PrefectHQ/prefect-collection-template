import re
import sys

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
PREFECT_COLLECTION_MODULE_REGEX = r"^prefect_[_a-zA-Z][_a-zA-Z0-9]+$"
PREFECT_COLLECTION_NAME_REGEX = r"^prefect-[-a-zA-Z][-a-zA-Z0-9]+$"

collection_slug = "{{cookiecutter.collection_slug}}"
collection_name = "{{cookiecutter.collection_name}}"

if not re.match(MODULE_REGEX, collection_slug):
    print(
        f"ERROR: The collection slug ({collection_slug}) is not a valid Python module name. "
        "Please do not use - and use _ instead"
    )
    sys.exit(1)

if not re.match(PREFECT_COLLECTION_MODULE_REGEX, collection_slug):
    print(
        f"ERROR: The collection slug ({collection_slug}) is not a valid Prefect collection module name. "
        "Please ensure your collection slug is prefixed with 'prefect_'"
    )
    sys.exit(1)

if not re.match(PREFECT_COLLECTION_NAME_REGEX, collection_name):
    print(
        "ERROR: The collection name ({collection_name}) is not a valid Prefect collection name. "
        "Please ensure your collection slug is prefixed with 'prefect-'"
    )
    sys.exit(1)
