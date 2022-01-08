from unittest import mock
from p1 import solution


def test_p1():
    mock.builtins.input = lambda: "hi"
    assert solution() == 'hi'
