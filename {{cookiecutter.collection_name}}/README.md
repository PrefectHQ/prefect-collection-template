# Coordinate and incorporate {{ cookiecutter.collection_name.split('-')[1:] | join | title}} in your dataflow with {{ cookiecutter.collection_name }}

<p align="center">
    <!--- Insert a cover image here
    <img src="I_usually_paste_the_image_on_github_UI_so_it_creates_link">
    -->
    <!--- <br> -->
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

Visit the full docs [here](https://{{ cookiecutter.github_organization }}.github.io/{{ cookiecutter.collection_name }}) to see additional examples and the API reference.

{{ cookiecutter.collection_short_description }}


<!--- ### Add a real-world example of how to use this Collection here

Offer some motivation on why this helps.

After installing `{{ cookiecutter.collection_name }}` and [saving the credentials](#saving-credentials-to-block), you can easily use it within your flows to help you achieve the aforementioned benefits!

```python
from prefect import flow, get_run_logger
```

--->

## Resources

For more tips on how to use tasks and flows in a Collection, check out [Using Collections](https://orion-docs.prefect.io/collections/usage/)!

### Installation

Install `{{ cookiecutter.collection_name }}` with `pip`:

```bash
pip install {{ cookiecutter.collection_name }}
```

A list of available blocks in `{{ cookiecutter.collection_name }}` and their setup instructions can be found [here](https://{{ cookiecutter.github_organization }}.github.io/{{ cookiecutter.collection_name }}/blocks-catalog).

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

<!--- ### Saving credentials to block

Replace this with actual instructions on how to get API key or token.

1. Head over to 
2. Login to your {{ cookiecutter.collection_name.split('-')[1:] | join | title}} account
3. Click "+ Create new secret key"
4. Copy the generated API key
5. Create a short script, replacing the placeholders (or do so in the UI)

```python
from {{ cookiecutter.collection_slug }} import Block`
Block(api_key="API_KEY_PLACEHOLDER").save("BLOCK_NAME_PLACEHOLDER")
```

Congrats! You can now easily load the saved block, which holds your credentials:

```python
from {{ cookiecutter.collection_slug }} import Block
Block.load("BLOCK_NAME_PLACEHOLDER")
```
--->

### Feedback

If you encounter any bugs while using `{{ cookiecutter.collection_name }}`, feel free to open an issue in the [{{ cookiecutter.collection_name }}](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}) repository.

If you have any questions or issues while using `{{ cookiecutter.collection_name }}`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to star or watch [`{{ cookiecutter.collection_name }}`](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}) for updates too!

### Contributing

If you'd like to help contribute to fix an issue or add a feature to `{{ cookiecutter.collection_name }}`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Here are the steps:

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```
pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:
```
pre-commit install
```
8. `git commit`, `git push`, and create a pull request
