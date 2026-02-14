import pytest
import sys
import os

# Добавляем путь к нашему модулю
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from myapp.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(10, 10) == 0

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0

def test_divide(calc):
    assert calc.divide(6, 2) == 3
    assert calc.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        calc.divide(1, 0)