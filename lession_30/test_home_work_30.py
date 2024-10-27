import pytest
import allure

@allure.feature("Множення")
@pytest.mark.parametrize("input_data, expected_output", [
    ([1, 2, 3], 6),
    ([2, 3, 4], 24),
    ([5, 5, 5], 125)
])
def test_multiply(input_data, expected_output):
    result = 1
    for number in input_data:
        result *= number
    assert result == expected_output

@allure.feature("Перевірка паліндрома")
@pytest.mark.parametrize("input_string, expected_output", [
    ("radar", True),
    ("hello", False),
    ("level", True),
    ("world", False)
])
def test_palindrome(input_string, expected_output):
    is_palindrome = input_string == input_string[::-1]
    assert is_palindrome == expected_output

@allure.feature("Перевірка довжини рядків")
@pytest.mark.parametrize("input_string, expected_length", [
    ("hello", 5),
    ("world", 5),
    ("", 0),
    ("Python", 6)
])
def test_string_length(input_string, expected_length):
    assert len(input_string) == expected_length
