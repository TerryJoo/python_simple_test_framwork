from io_test_function import io_test_function
from p3 import solution


def test_p3_1():
    io_test_function(solution, '5\n0 1 2\n3 4 5', '5\n0 1 2\n3 4 5')


def test_p3_2():
    io_test_function(solution, '1\n2 2 2\n3 3 3', '1\n2 2 2\n3 3 3')
