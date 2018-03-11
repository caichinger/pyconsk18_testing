import pytest

def fun():
    raise ZeroDivisionError()

def test_fun_raises_zero_division_error():
    with pytest.raises(TypeError):
        fun()