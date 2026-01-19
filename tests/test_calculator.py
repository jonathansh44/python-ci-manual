import pytest
from services.calculator_service import add, divide, subtract, multiply


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5

def test_subtract():
    assert subtract(5, 3) == 1

def test_multiply():
    assert multiply(4, 3) == 15

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
