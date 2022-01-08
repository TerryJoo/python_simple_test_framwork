from unittest import mock
from p3 import solution


def test_p3():
    mock.builtins.input = lambda: "hi"
    assert solution() == 'hi'
