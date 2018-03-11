"""
Complete/fix these tests.
"""
import pytest

import numpy as np
import pandas as pd


def test_comparing_list():
    assert [1, 2, 3] == [1, 3]

    
def test_comparing_dict():
    assert {'a': 1, 'b': 2} == {'c': 2, 'a': 1}

    
def test_comparing_numbers():
    assert (0.1 + 0.1 + 0.1) / 3 == 0.1

    
def test_comparing_numpy_arrays():
    assert np.array([1, 2, 3.1]) == np.array([1, 2, 3])

    
def test_comparing_dataframes():
    assert pd.DataFrame({'a': [1, 2], 'b': [3, 4]}) == pd.DataFrame({'b': [3., 4.], 'a': [1, 2]})

    
def some_exception():
    raise ZeroDivisionError('O.o')
    
    
def test_some_exception():
    # check that ZeroDivisionError is raised with 'O.o'
    pass


def multiply(a, b):
    """
    >>> multiply(1, 2)
    2
    >>> multiply([3], 3)
    [3, 3, 3]
    """
    return a * b


def test_multiply():
    # run doctest using pytest
    # make parametrized test case based on doctests
    pass


if __name__ == '__main__':
    pytest.main([__file__])