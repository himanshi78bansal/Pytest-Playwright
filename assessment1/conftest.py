import pytest

# task 1
@pytest.fixture(scope="session")
def setup():
    print("Browser setup")
    yield
    print("Browser teardown")
