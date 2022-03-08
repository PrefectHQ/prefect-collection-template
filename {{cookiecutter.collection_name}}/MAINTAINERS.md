# {{ cookiecutter.collection_name }}

## Getting Started

### Python setup

Requires an installation of Python 3.7+

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

### Project setup

To setup your project run the following:

```bash
# Create an editable install of your project
pip install -e ".[dev]"

# Configure pre-commit hooks
pre-commit install
```

To verify the set up was successful you can run the following:

- Run the tests for tasks and flows in the collection:
  ```bash
  pytest tests
  ```
- Serve the docs with `mkdocs`:
  ```bash
  mkdocs serve
  ```

## Developing tasks and flows

For information about the use and development of tasks and flow, check out the [flows](https://orion-docs.prefect.io/concepts/flows/) and [tasks](https://orion-docs.prefect.io/concepts/tasks/) concepts docs in the Prefect docs.

## Writing documentation

This collection has been setup to with [mkdocs](https://www.mkdocs.org/) for automatically generated documentation. The signatures and docstrings of your tasks and flow will be used to generate documentation for the users of this collection. You can make changes to the structure of the generated documentation by editing the `mkdocs.yml` file in this project.

## Development lifecycle

### CI Pipeline

This collection comes with [GitHub Actions](https://docs.github.com/en/actions) for testing and linting. To add additional actions, you can add jobs in the `.github/workflows` folder. On PR, the pipeline will run linting via [`black`](https://black.readthedocs.io/en/stable/) and [`flake8`](https://flake8.pycqa.org/en/latest/) and unit tests via `pytest`.

### Package and Publish

GitHub actions will handle packaging and publishing of your collection to [PyPI](https://pypi.org/) so other Prefect users can your collection in their flows.

In order to publish to PyPI, you'll need a PyPI account and generate an API token to authenticate with PyPI when publishing new versions of your collection. The [PyPI documentation](https://pypi.org/help/#apitoken) outlines the steps needed to get an API token.

Once you've obtained a PyPI API token, [create a GitHub secret](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) named `PYPI_API_TOKEN`.

To create publish a new version of your collection, [create a new GitHub release](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository#creating-a-release) and tag it with the version that you want to deploy (e.g. v0.3.2). This will trigger workflow to publish the new version on PyPI and deploy the updated docs to GitHub pages.

## Further guidance

If you run into any issues during the bootstrapping process, feel free to open an issue in the [prefect-collection-template](https://github.com/PrefectHQ/prefect-collection-template) repository.

If you have any questions or issues while developing your collection, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).
