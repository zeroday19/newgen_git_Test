import pytest

from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.fixture
def dataset():
    return {"x": 5, "y": 4, "a": 9, "s": 1, "m": 20, "d": 1.25}


