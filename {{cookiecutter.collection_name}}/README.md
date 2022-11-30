# {{ cookiecutter.collection_name }}

<p align="center">
    <a href="https://pypi.python.org/pypi/{{ cookiecutter.collection_name }}/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/{{ cookiecutter.collection_name }}?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}/" alt="Stars">
        <img src="https://img.shields.io/github/stars/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/{{ cookiecutter.collection_name }}/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/{{ cookiecutter.collection_name }}?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

## Welcome!

{{ cookiecutter.collection_short_description }}

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

Then, register to [view the block](https://orion-docs.prefect.io/ui/blocks/) on Prefect Cloud:

```bash
prefect block register -m {{ cookiecutter.collection_slug }}
```

Note, to use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

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

If you encounter any bugs while using `{{ cookiecutter.collection_name }}`, feel free to open an issue in the [{{ cookiecutter.collection_name }}](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}) repository.

If you have any questions or issues while using `{{ cookiecutter.collection_name }}`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to ⭐️ or watch [`{{ cookiecutter.collection_name }}`](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}) for updates too!

## Development

If you'd like to install a version of `{{ cookiecutter.collection_name }}` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}.git

cd {{ cookiecutter.collection_name }}/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
