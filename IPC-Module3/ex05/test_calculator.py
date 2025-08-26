import pytest
import calculator

def test_add() -> None:
    """test referring to the sum function"""
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-5, -7) == -12
    assert calculator.add(0, 0) == 0
    assert calculator.add(1_000_000, 2_000_000) == 3_000_000


def test_subtract() -> None:
    """test referring to the subtract function"""
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 15) == -5
    assert calculator.subtract(-5, -5) == 0
    assert calculator.subtract(0, 10) == -10
    assert calculator.subtract(10, 0) == 10


def test_multiply() -> None:
    """test referring to the multiply function"""
    assert calculator.multiply(3, 4) == 12
    assert calculator.multiply(-2, 5) == -10
    assert calculator.multiply(-3, -6) == 18
    assert calculator.multiply(0, 100) == 0
    assert calculator.multiply(12345, 0) == 0
    assert calculator.multiply(1_000, 1_000) == 1_000_000


def test_divide() -> None:
    """test referring to the dvide function"""
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(9, 4) == 2.25
    assert calculator.divide(7, 4) == 1.75
    assert calculator.divide(-9, 3) == -3.0
    assert calculator.divide(-9, -3) == 3.0
    assert calculator.divide(0, 5) == 0.0


def test_power() -> None:
    """test referring to the power of x and y function"""
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(0, 5) == 0
    assert calculator.power(2, -2) == 0.25
    assert calculator.power(-2, 3) == -8
    assert calculator.power(-2, 2) == 4

def test_divide_by_zero() -> None:
    """test referring to raise error when divide per 0"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)
