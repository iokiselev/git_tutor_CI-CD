import pytest
from calculator import add, subtracting, multiply, square, divide


@pytest.mark.add
def test_add_ok():
    assert add(5, 10) == 15


@pytest.mark.subtracting
def test_subtracting_ok():
    assert subtracting(5, 10) == -5


@pytest.mark.multiply
def test_multiply_ok():
    assert multiply(3, 5) == 15


@pytest.mark.square
def test_square_ok():
    assert square(3, 3) == 27


@pytest.mark.divide
def test_divide_ok():
    assert divide(10, 5) == 2
