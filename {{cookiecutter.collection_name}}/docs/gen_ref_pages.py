"""
Copies README.md to index.md. Also discovers all blocks and
generates a list of them in the docs under the Blocks Catalog heading.
"""

import re
from collections import defaultdict
from inspect import getmembers, isclass, isfunction, ismodule
from pathlib import Path
from textwrap import dedent
from typing import Any, Set

import mkdocs_gen_files
from griffe.dataclasses import Docstring
from griffe.docstrings.dataclasses import DocstringSectionKind
from griffe.docstrings.parsers import Parser, parse
from prefect.blocks.core import Block
from prefect.logging.loggers import disable_logger
from prefect.utilities.dispatch import get_registry_for_type
from prefect.utilities.importtools import to_qualified_name

import {{ cookiecutter.collection_slug }}

COLLECTION_SLUG = "{{ cookiecutter.collection_slug }}"

# Home page


readme_path = Path("README.md")
docs_index_path = Path("index.md")

with open(readme_path, "r") as readme:
    with mkdocs_gen_files.open(docs_index_path, "w") as generated_file:
        for line in readme:
            if line.startswith("Visit the full docs [here]("):
                continue  # prevent linking to itself
            generated_file.write(line)

    mkdocs_gen_files.set_edit_path(Path(docs_index_path), readme_path)

# Blocks Catalog page


def find_module_blocks():
    blocks = get_registry_for_type(Block)
    collection_blocks = [
        block
        for block in blocks.values()
        if to_qualified_name(block).startswith(COLLECTION_SLUG)
    ]
    module_blocks = {}
    for block in collection_blocks:
        block_name = block.__name__
        module_nesting = tuple(to_qualified_name(block).split(".")[1:-1])
        if module_nesting not in module_blocks:
            module_blocks[module_nesting] = []
        module_blocks[module_nesting].append(block_name)
    return module_blocks


def insert_blocks_catalog(generated_file):
    module_blocks = find_module_blocks()
    if len(module_blocks) == 0:
        return
    generated_file.write(
        dedent(
            f"""
            Below is a list of Blocks available for registration in
            `"{{ cookiecutter.collection_name }}"`.

            To register blocks in this module to
            [view and edit them](https://orion-docs.prefect.io/ui/blocks/)
            on Prefect Cloud:
            ```bash
            prefect block register -m {COLLECTION_SLUG}
            ```
            """
        )
    )
    generated_file.write(
        "Note, to use the `load` method on Blocks, you must already have a block document "  # noqa
        "[saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) "  # noqa
        "or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).\n"
    )
    for module_nesting, block_names in module_blocks.items():
        module_path = " ".join(module_nesting)
        module_title = module_path.replace("_", " ").title()
        generated_file.write(
            f"## [{module_title} Module][{COLLECTION_SLUG}.{module_path}]\n"
        )
        for block_name in block_names:
            generated_file.write(
                f"[{block_name}][{COLLECTION_SLUG}.{module_path}.{block_name}]\n"
            )
            generated_file.write(
                dedent(
                    f"""
                    To load the {block_name}:
                    ```python
                    from prefect import flow
                    from {COLLECTION_SLUG}.{module_path} import {block_name}

                    @flow
                    def my_flow():
                        my_block = {block_name}.load("MY_BLOCK_NAME")

                    my_flow()
                    ```
                    """
                )
            )


blocks_catalog_path = Path("blocks_catalog.md")
with mkdocs_gen_files.open(blocks_catalog_path, "w") as generated_file:
    insert_blocks_catalog(generated_file)

# Examples Catalog page


def skip_parsing(name, obj, module_nesting):
    """
    Skips parsing the object if it's a private method or if it's not in the
    right module.
    """
    try:
        wrong_module = not to_qualified_name(obj).startswith(module_nesting)
    except AttributeError:
        wrong_module = False
    return obj.__doc__ is None or name.startswith("_") or wrong_module


def skip_code_example(code_example: str) -> bool:
    """
    Skips the code example if it's just showing how to load a Block.
    """
    return re.search(r'\.load\("BLOCK_NAME"\)\s*$', code_example.rstrip("`"))


def get_code_examples(obj: Any) -> Set[str]:
    """
    Gathers all the code examples within an object.
    """
    code_examples = set()
    with disable_logger("griffe.docstrings.google"):
        with disable_logger("griffe.agents.nodes"):
            docstring = Docstring(obj.__doc__)
            parsed_sections = parse(docstring, Parser.google)

    for section in parsed_sections:
        if section.kind == DocstringSectionKind.examples:
            code_example = "\n".join(
                (part[1] for part in section.as_dict().get("value", []))
            )
            if not skip_code_example(code_example):
                code_examples.add(code_example)
        if section.kind == DocstringSectionKind.admonition:
            value = section.as_dict().get("value", {})
            if value.get("annotation") == "example":
                code_example = value.get("description")
                if not skip_code_example(code_example):
                    code_examples.add(code_example)

    return code_examples


code_examples_grouping = defaultdict(set)
for module_name, module_obj in getmembers({{ cookiecutter.collection_slug }}, ismodule):

    module_nesting = f"{COLLECTION_SLUG}.{module_name}"
    # find all module examples
    if skip_parsing(module_name, module_obj, module_nesting):
        continue
    code_examples_grouping[module_name] |= get_code_examples(module_obj)

    # find all class and method examples
    for class_name, class_obj in getmembers(module_obj, isclass):
        if skip_parsing(class_name, class_obj, module_nesting):
            continue
        code_examples_grouping[module_name] |= get_code_examples(class_obj)
        for method_name, method_obj in getmembers(class_obj, isfunction):
            if skip_parsing(method_name, method_obj, module_nesting):
                continue
            code_examples_grouping[module_name] |= get_code_examples(method_obj)

    # find all function examples
    for function_name, function_obj in getmembers(module_obj, isfunction):
        if skip_parsing(function_name, function_obj, module_nesting):
            continue
        code_examples_grouping[module_name] |= get_code_examples(function_obj)

examples_catalog_path = Path("examples_catalog.md")
with mkdocs_gen_files.open(examples_catalog_path, "w") as generated_file:
    generated_file.write(
        dedent(
            """
            # Examples Catalog

            Below is a list of examples for `{{ cookiecutter.collection_name }}`.
            """
        )
    )
    for module_name, code_examples in code_examples_grouping.items():
        if len(code_examples) == 0:
            continue
        module_title = module_name.replace("_", " ").title()
        generated_file.write(
            f"## [{module_title} Module][{COLLECTION_SLUG}.{module_name}]\n"
        )
        for code_example in code_examples:
            generated_file.write(code_example + "\n")
