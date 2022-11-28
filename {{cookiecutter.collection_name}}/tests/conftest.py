import pytest
from prefect.testing.utilities import prefect_test_harness


@pytest.fixture(scope="session", autouse=True)
def prefect_db():
    """
    Sets up test harness for temporary DB during test runs.
    """
    with prefect_test_harness():
        yield


@pytest.fixture(autouse=True)
def reset_object_registry():
    """
    Ensures each test has a clean object registry.
    """
    from prefect.context import PrefectObjectRegistry

    with PrefectObjectRegistry():
        yield


@pytest.fixture
def caplog(caplog):
    """
    Overrides caplog to apply to all of our loggers that do not propagate and
    consequently would not be captured by caplog.
    """

    config = setup_logging()

    for name, logger_config in config["loggers"].items():
        if not logger_config.get("propagate", True):
            logger = get_logger(name)
            logger.handlers.append(caplog.handler)

    yield caplog
