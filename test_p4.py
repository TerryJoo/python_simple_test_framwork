from unittest import mock
from p4 import solution


def test_p4():
    mock.builtins.input = lambda: "hi"
    assert solution() == 'hi'
