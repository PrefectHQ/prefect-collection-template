# {{ cookiecutter.collection_name }}

## Welcome!

{{ cookiecutter.collection_name }} is a collection of prebuilt Prefect tasks that can be used to quickly construct Prefect flows.

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `{{ cookiecutter.collection_name }}` with `pip`:

```bash
pip install {{ cookiecutter.collection_name }}
```

### Write and run a flow

```python
from prefect import flow
from {{ cookiecutter.collection_slug }}.tasks import (
    goodbye_{{ cookiecutter.collection_slug }},
    hello_{{ cookiecutter.collection_slug }},
)


@flow
def example_flow():
    hello_{{ cookiecutter.collection_slug }}
    goodbye_{{ cookiecutter.collection_slug }}

example_flow()
```

## Resources

If you encounter and bugs while using `{{ cookiecutter.collection_name }}`, feel free to open an issue in the [{{ cookiecutter.collection_name }}](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}) repository.

If you have any questions or issues while using `{{ cookiecutter.collection_name }}`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `{{ cookiecutter.collection_name }}` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}.git

cd {{ cookiecutter.collection_name }}/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
