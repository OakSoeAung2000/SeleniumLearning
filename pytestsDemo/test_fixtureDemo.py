import pytest


@pytest.fixture()
def setup():
    print("i will be executing")
    yield
    print("Last executed")

def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")