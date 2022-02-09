# prefect-collection

## Welcome!

prefect-collection is a collections of prebuilt Prefect tasks that can be used to quickly construct Prefect flows.

## Getting Started

### Python setup

Requires an installation of Python 3.7+

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect` and `prefect-collection`

```bash
pip install "prefect>=2.0a9" prefect-aws
```

### Write and run a flow

```python
from prefect import flow
import prefect_collection

@flow
def example_flow():
    """
    TODO: Document example flow
    """
    pass

example_flow()
```

## Development

If you'd like to install a version of prefect-collection for development, first clone the prefect-collection repository and then install in editable mode with `pip`:

```bash
git clone https://github.com/arthur_dent/prefect-collection.git
cd prefect-collection/
pip install -e ".[dev]"
```
