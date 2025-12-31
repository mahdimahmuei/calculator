
import pytest
from calculator.main import adder, sub, multiply, divider


def test_adder():
    assert adder(2, 3) == 5
    assert adder(-1, 1) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(3, 5) == -2


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(0, 10) == 0


def test_divider():
    assert divider(10, 2) == 5
    assert divider(3, 2) == 1.5
