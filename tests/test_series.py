from math_series.series import fibonacci
from math_series.series import Lucas
from math_series.series import sum_series

## testing for fibonacci series

def test_fibonacci_series_of_index_0():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_fibonacci_series_of_index_1():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual

def test_fibonacci_series_of_index_6():
    expected = 8
    actual = fibonacci(6)
    assert expected == actual


## testing for Lucas series

def test_lucas_series_of_index_0():
    expected = 2
    actual = Lucas(0)
    assert expected == actual


def test_lucas_series_of_index_1():
    expected = 1
    actual = Lucas(1)
    assert expected == actual


def test_lucas_series_of_index_6():
    expected = 18
    actual = Lucas(6)
    assert expected == actual


## sum series testing

def test_sum_series_4():
    expected = 3
    actual = sum_series(4)
    assert expected == actual

def test_sum_series_5_3():
    expected = 14
    actual = sum_series(5,3)
    assert expected == actual

def test_sum_series_4_None_3():
    expected = 15
    actual = sum_series(5,None, 3)
    assert expected == actual

def test_sum_series_4_2_3():
    expected = 13
    actual = sum_series(4,2,3)
    assert expected == actual