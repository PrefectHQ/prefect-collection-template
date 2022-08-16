from pydantic import Field

from prefect.blocks.core import Block


class {{ cookiecutter.collection_name.split('-')[1:] | join }}Block(Block):
    """
    A sample block that holds a value.

    Args:
        value (str): The value to store.
    
    Example:
        Load a stored value:
        ```python
        from {{ cookiecutter.collection_slug }} import {{ cookiecutter.collection_name.split('-')[1:] | join }}Block
        block = {{ cookiecutter.collection_name.split('-')[1:] | join }}Block.load("BLOCK_NAME")
        ```
    """

    value: str = Field("The default value", description="The value to store")

    @classmethod
    def seed_value_for_example(cls):
        block = cls(value="A sample value")
        block.save("sample-block")
