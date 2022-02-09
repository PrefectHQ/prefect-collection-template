# prefect-collection

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

If all those actions were successful, then you are all ready to start creating your Prefect collection!

If you run into any issues during the bootstrapping process, feel free to open an issue in the [prefect-collection-template](https://github.com/PrefectHQ/prefect-collection-template) repository.