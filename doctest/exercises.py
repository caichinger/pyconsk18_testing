"""
Doctest Exercises.
"""

def fancy_plot():
    fig, ax = plt.subplots()
    ax.plot([1, 2])
    return ax

def possible_unordered_return_value():
    return {'b': 2, 'a': 1}

def many_digit_number():
    return 1/42

def some_exception():
    raise ZeroDivisionError('O.o')

def multiply(a, b):
    """
    Computes a * b
    
    >>> multiply(['A', 'B'], 2)
    ['A', 'B',
     'A', 'B']    
    """
    return a * b