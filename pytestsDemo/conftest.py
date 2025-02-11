import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing")
    yield
    print("Last executed")

@pytest.fixture(scope="class")
def dataLoad():
    print("user profile data is being created")
    return ["oak", "soe", "oaksoe146@gmail.com"]\

@pytest.fixture(params=[("chrome","oak", "soe"), ("Firefox", "oak"), "IE"])
def crossBrowser(request):
    return request.param
