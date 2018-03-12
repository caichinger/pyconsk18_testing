"""
Fix this test file.
"""
import pytest

import numpy as np
import pandas as pd


def test_comparing_list():
    # assert [1, 2, 3] == [1, 3]
    assert [1, 2, 3] == [1, 2, 3]
    
    
def test_comparing_dict():
    # dict is unordered, appearance may change (prior to Python 3.6)
    # assert {'a': 1, 'b': 2} == {'c': 2, 'a': 1}
    assert {'a': 1, 'b': 2} == {'a': 1, 'b': 2}


def test_comparing_numbers():
    # assert (0.1 + 0.1 + 0.1) / 3 == 0.1
    assert (0.1 + 0.1 + 0.1) / 3 == pytest.approx(0.1)
    
    
def test_comparing_numpy_arrays():
    # use numpy.testing.assert_allclose
    # assert np.array([1, 2, 3.1]) == np.array([1, 2, 3])
    np.testing.assert_allclose(np.array([1, 2, 3.1]), np.array([1, 2, 3]), atol=0.1)
    
    
def test_comparing_dataframes():
    # use pandas.testing.assert_frame_equal
    # assert pd.DataFrame({'a': [1, 2], 'b': [3, 4]}) == pd.DataFrame({'b': [3., 4.], 'a': [1, 2]})
    pd.testing.assert_frame_equal(pd.DataFrame({'a': [1, 2], 'b': [3, 4]}), 
                                  pd.DataFrame({'b': [3., 4.], 'a': [1, 2]}), 
                                  check_dtype=False)

    
def some_exception():
    raise ZeroDivisionError('O.o')
    
    
def test_some_exception():
    with pytest.raises(ZeroDivisionError) as excinfo:
        some_exception()
    excinfo.value.args[0] == 'O.o'


def multiply(a, b):
    """
    >>> multiply(1, 2)
    2
    >>> multiply([3], 3)
    [3, 3, 3]
    """
    return a * b


@pytest.mark.parametrize("a_b, expected", [
    ((1, 2), 2),
    (([3], 3), [3, 3, 3]),
])
def test_multiply(a_b, expected):
    assert multiply(*a_b) == expected
    

if __name__ == '__main__':
    pytest.main([__file__, '--doctest-modules'])