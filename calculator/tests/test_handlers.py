import pytest
import mock

from calculator.handlers import (
    available_operations, compute, format_operations_to_string, should_stop, read_number, read_operation
)


def test_format_operations_to_string():
    result = format_operations_to_string()
    assert result == "+, -, *, /, ="


@pytest.mark.parametrize("keyboard_input", ["3", "a"])
def test_read_number(keyboard_input):
    with mock.patch("builtins.input", return_value=keyboard_input):
        try:
            int_keyboard_input = int(keyboard_input)
            returned_number = read_number()
            assert returned_number == int_keyboard_input
        except ValueError:
            # This will result in an infinite loop.
            pass


@pytest.mark.parametrize("keyboard_input", ["+", "-", "*", "/", "=", "a", "b", "7"])
def test_read_operation(keyboard_input):
    with mock.patch("builtins.input", return_value=keyboard_input):
        if keyboard_input in available_operations:
            returned_operation = read_operation()
            assert returned_operation == keyboard_input
        else:
            # This will result in an infinite loop
            pass


@pytest.mark.parametrize("operation, expected_result", [
    ("+", False),
    ("-", False),
    ("*", False),
    ("/", False),
    ("=", True),
])
def test_should_stop(operation, expected_result):
    assert should_stop(operation) is expected_result


@pytest.mark.parametrize("first_operand, second_operand, operation, expected_result", [
    (3, 5, "+", 8),
    (7, 2, "-", 5),
    (4, 4, "*", 16),
    (8, 2, "/", 4),
    (21, 0, "/", None),
    (10, None, "=", 10),
])
def test_compute(first_operand, second_operand, operation, expected_result):
    mocked_keyboard_input = "7"
    with mock.patch("builtins.input", return_value=mocked_keyboard_input):
        result = compute(first_operand, second_operand, operation)

        if second_operand == 0 and operation == "/":
            assert result == first_operand / int(mocked_keyboard_input)
        else:
            assert result == expected_result
