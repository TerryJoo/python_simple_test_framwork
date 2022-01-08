from unittest import mock
from p1 import solution
import io
from contextlib import redirect_stdout


def inputs():
    yield '5'
    yield '0 1 2'
    yield '3 4 5'


def test_p1():
    f = io.StringIO()
    multi_line_inputs = inputs()
    mock.builtins.input = lambda: multi_line_inputs.__next__()
    with redirect_stdout(f):
        solution()
    out = f.getvalue()
    assert out == '5\n0 1 2\n3 4 5' + '\n'

