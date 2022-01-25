from unittest import mock
import io
from contextlib import redirect_stdout


def io_test(solution, input_data, output):
    def inputs(lines):
        for line in lines.split('\n'):
            yield line

    f = io.StringIO()
    multi_line_inputs = inputs(input_data)
    mock.builtins.input = lambda: multi_line_inputs.__next__()
    with redirect_stdout(f):
        solution()
    out = f.getvalue()
    assert out == output + '\n'
