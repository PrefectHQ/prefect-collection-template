# {{ cookiecutter.collection_name }}

Welcome to your new Prefect collection! Feel free to modify this README to fit the needs of your collection!

## Getting Started

### Python setup

Requires an installation of Python 3.7+

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

### Verify collection bootstrap

To ensure that your collection bootstrap was successful you can perform the following steps:

1. Create an editable install of your project
   ```bash
   pip install -e ".[dev]
   ```
2. Run the tests for the example tasks and flow in the bootstrapped collection
   ```bash
   pytest tests
   ```
3. Serve the bootstrapped example docs with `mkdocs`
   ```bash
   mkdocs serve
   ```

You are now ready to start creating your Prefect collection!

## Developing tasks and flows

For information about the use and development of tasks and flow, check out the [flows](https://orion-docs.prefect.io/concepts/flows/) and [tasks](https://orion-docs.prefect.io/concepts/tasks/) concepts docs in the Prefect docs.

## Writing documentation

This collection has been setup to with [mkdocs](https://www.mkdocs.org/) for automatically generated documentation. The signatures and docstrings of your tasks and flow will be used to generate documentation for the users of this collection. You can make changes to the structure of the generated documentation by editing the `mkdocs.yml` file in this project.

## Development lifecycle

This collection comes with [GitHub Actions](https://docs.github.com/en/actions) for testing and linting. To add additional actions, you can add jobs in the `.github/workflows` folder.

## Further guidance

If you run into any issues during the bootstrapping process, feel free to open an issue in the [prefect-collection-template](https://github.com/PrefectHQ/prefect-collection-template) repository.

If you have any questions or issues while developing your collection, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack)
