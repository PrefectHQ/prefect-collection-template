# prefect-collection-template

## Welcome!

`prefect-collection-template` is a [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template for quickly bootstrapping a Prefect Collection.

When you bootstrap a Prefect Collection with `prefect-collection-template` you'll automatically be set up with the tools necessary to build and maintain your collection:

- [`mkdocs`](https://www.mkdocs.org/) for automatic documentation generation
- [`black`](https://github.com/psf/black), [`isort`](https://github.com/PyCQA/isort), and [`flake8`](https://flake8.pycqa.org/en/latest/) for automatic code formatting and linting
- [`pytest`](https://docs.pytest.org/en/7.1.x/) for unit testing
- [`interrogate`](https://interrogate.readthedocs.io/en/latest/) for documentation coverage analysis
- [`Coverage.py`](https://coverage.readthedocs.io/en/6.3.2/) for code coverage analysis
- [`pre-commit`](https://pre-commit.com/) to automatically run code formatting and linting prior to git commit
- [`versioneer`](https://github.com/python-versioneer/python-versioneer) for automatic package versioning
- [GitHub Actions](https://docs.github.com/en/actions) workflows for continuous integration and deployment of your collection and its documentation

We're excited to see what you build!

## Quickstart

Install `cruft` if you have not already:

```bash
pip install cruft
```

Generate a Prefect Collection project:

```
cruft create https://github.com/PrefectHQ/prefect-collection-template
```

Refer to the MAINTAINERS.md in the generated project for how to get started developing Prefect tasks and flow.

## Contributing

To start contributing to `prefect-collection-template`, run:

```bash
pip install -r requirements-dev.txt
```

To test generation of a Prefect Collection with your changes, run:

```
cruft create .
```

To run tests, from the base directory of the repository, run:

```bash
pytest tests
```
