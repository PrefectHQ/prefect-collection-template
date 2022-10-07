from . import _version
from .blocks import {{ cookiecutter.collection_name.split('-')[1:] | join | title}}Block  # noqa

__version__ = _version.get_versions()["version"]
