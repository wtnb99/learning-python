import pytest

from hello import say_hello


def test_say_hello():
    assert say_hello("Taro") == "Hello, Taro"
    assert say_hello("Jiro") == "Hello, Jiro"
    assert say_hello() != "Hello, Taro"
