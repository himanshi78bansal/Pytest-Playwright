import pytest


# task 2

@pytest.mark.smoke
def test_smoke_example(setup):
    print("Executing smoke test")

@pytest.mark.regression
def test_regression_example(setup):
    print("Executing regression test")


@pytest.mark.skip(reason="Not required now")
def test_skip_example(setup):
    print("Executing skip test")
