<!-- 
Thanks for opening a pull request to {{ cookiecutter.collection_name }} 🎉!

Please make sure that your title neatly summarizes the proposed changes.
-->

<!-- Overview -->

Closes

### Example
<!-- A code blurb is best. Changes to features should include an example that is executable by a new user. -->

### Screenshots
<!--
Any relevant screenshots, e.g.
- the updated docs page from `mkdocs serve`
- output from running the example
- service integration test results
-->

### Checklist
<!-- These boxes may be checked after opening the pull request. -->

- [ ] References any related issue by including "Closes #<ISSUE_NUMBER>" or "Closes <Issue URL>"
	- If no issue exists and your change is not a small fix, please [create an issue](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}/issues/new/choose) first.
- [ ] Includes tests or only affects documentation.
- [ ] Passes `pre-commit` checks.
  - Run `pre-commit install && pre-commit run --all` locally for formatting and linting.
- [ ] Includes screenshots of documentation updates.
  - Run `mkdocs serve` view documentation locally.
- [ ] Summarized PR's changes in [CHANGELOG.md](https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.collection_name }}/blob/main/CHANGELOG.md)
