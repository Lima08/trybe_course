from nis import match
import pytest 
from divide import divide


def test_divide_when_number_is_zero_raises_an_excepition():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
        divide(2, 0)


def test_divide_when_number_is_one():
    assert divide(2, 1) == 2.0
