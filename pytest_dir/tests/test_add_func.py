import pytest

from src import add_func
import add_func2


def test_add_func():
    assert add_func.add_func(1, 2) == 3


def test_add_func2():
    assert add_func2.add_func2(1, 2) == 3
