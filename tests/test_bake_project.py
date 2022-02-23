from cookiecutter.exceptions import FailedHookException
from cookiecutter.utils import rmtree
from contextlib import contextmanager
import os
import subprocess
import shlex


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        if result.project is not None:
            rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_bake_with_defaults(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        assert result.project_path.name == "prefect-collection"

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "setup.py" in found_toplevel_files
        assert "requirements.txt" in found_toplevel_files
        assert "requirements_dev.txt" in found_toplevel_files
        assert "prefect_collection" in found_toplevel_files
        assert "README.md" in found_toplevel_files
        assert "tests" in found_toplevel_files
        assert ".github" in found_toplevel_files
        assert "docs" in found_toplevel_files
        assert "mkdocs.yml" in found_toplevel_files
        assert ".gitignore" in found_toplevel_files
        assert "LICENSE" in found_toplevel_files


def test_bake_with_custom_name(cookies):
    context = {"collection_name": "prefect-awesome"}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        assert result.project_path.name == "prefect-awesome"
        assert (result.project_path / "prefect_awesome").exists


def test_bake_and_run_tests(cookies):
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir('pip install -e ".[dev]"', str(result.project)) == 0
        assert run_inside_dir("pytest tests", str(result.project)) == 0
        print("test_bake_and_run_tests path", str(result.project))


def test_bake_with_underscore_name_fail(cookies):
    context = {"collection_name": "prefect_awesome"}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert isinstance(result.exception, FailedHookException)


def test_bake_with_hyphen_slug_fail(cookies):
    context = {"collection_slug": "prefect-awesome"}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert isinstance(result.exception, FailedHookException)
