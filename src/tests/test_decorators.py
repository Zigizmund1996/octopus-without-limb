import pytest
from src.decorators import log
import os

log_path = os.path.join("logs", "mylogs.txt")


@log(filename="log_path")
def my_function(x, y):
    return x + y


@log()
def my_function_console(x, y):
    return x + y


def test_my_function_file(tmp_path):
    log_file = tmp_path / "testlog.txt"

    @log(filename=log_file)
    def test_function(x, y):
        return x * y

    result = test_function(2, 3)
    assert result == 6

    with open(log_file, "r") as f:
        log_content = f.read()

    assert "Started execution of test_function" in log_content
    assert "Finished execution of test_function with result: 6" in log_content


def test_my_function_console(capsys):
    result = my_function_console(3, 2)
    captured = capsys.readouterr()

    assert result == 5
    assert "Started execution of my_function_console" in captured.out
    assert "Finished execution of my_function_console with result: 5" in captured.out
