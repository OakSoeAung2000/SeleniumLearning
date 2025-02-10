#any pytest file should start with test_
import pytest


@pytest.mark.smoke
def test_fristProgram():
    print("Hello")

def test_secondProgram():
    print("Good Morning")