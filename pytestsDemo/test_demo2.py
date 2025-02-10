#any pytest file should start with test_ or end with _test
#-k stand for method name execution
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed"

@pytest.mark.xfail
def test_secondProgram():
    a = 4
    b = 6
    assert a + b == 10 , "Test failed"

@pytest.fixture()
def setup():
    print("i will be executing")

def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")