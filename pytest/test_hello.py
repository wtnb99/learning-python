import pytest

from hello import say_hello
from hello import extract_pattern


def test_say_hello():
    assert say_hello("Taro") == "Hello, Taro"
    assert say_hello("Jiro") == "Hello, Jiro"
    assert say_hello() == "Hello, Taro"


def test_extract_pattern():
    text = "Z PASS S001"
    assert extract_pattern(text) == ("PASS", "S001")
    text = "m FAIL S001"
    assert extract_pattern(text) == ("FAIL", "S001")
    text = "] PASS S002"
    assert extract_pattern(text) == ("PASS", "S002")
    text = "\\ FAIL S002"
    assert extract_pattern(text) == ("FAIL", "S002")
