import math
from src.main import calculate_sqrt

def test_sqrt_of_4():
    result = calculate_sqrt(4, 2)
    assert math.isclose(result, 2.0, abs_tol=0.01)

def test_sqrt_of_9():
    result = calculate_sqrt(9, 3)
    assert math.isclose(result, 3.0, abs_tol=0.001)

def test_sqrt_of_16():
    result = calculate_sqrt(16, 5)
    assert math.isclose(result, 4.0, abs_tol=0.00001)

def test_sqrt_of_25():
    result = calculate_sqrt(25, 4)
    assert math.isclose(result, 5.0, abs_tol=0.0001)

def test_sqrt_of_1():
    result = calculate_sqrt(1, 5)
    assert math.isclose(result, 1.0, abs_tol=0.00001)

def test_sqrt_of_100():
    result = calculate_sqrt(100, 2)
    assert math.isclose(result, 10.0, abs_tol=0.01)

def test_sqrt_of_0():
    result = calculate_sqrt(0, 3)
    assert math.isclose(result, 0.0, abs_tol=0.001)

def test_sqrt_of_negative_number():
    result = calculate_sqrt(-16, 5)
    assert result is None

def test_sqrt_of_very_small_number():
    result = calculate_sqrt(0.000001, 5)
    assert math.isclose(result, 0.001, abs_tol=0.00001)