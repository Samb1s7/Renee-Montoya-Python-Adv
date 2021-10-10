import pytest
from functions_to_test import *


calc = Calculator

def test_add():
    assert calc.add(3,5) == 8

def test_subtract():
    assert calc.subtract(8,5) == 3

def test_multiply():
    assert calc.multiply(4, 3) == 12

def test_divide():
    assert calc.divide(9,3) == 3
    with pytest.raises(ValueError):
        calc.divide(3,0)
