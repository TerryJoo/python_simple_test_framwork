from unittest import mock
from p2 import solution


def test_p2():
    mock.builtins.input = lambda: "hi"
    assert solution() == 'hi'
