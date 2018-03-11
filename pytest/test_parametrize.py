import pytest

def inc(x):
    return x + 1

@pytest.mark.parametrize('x, expected', [
    (1, 2),
    (4, 5),
    (10, 101),
])
def test_inc(x, expected):
    assert inc(x) == expected