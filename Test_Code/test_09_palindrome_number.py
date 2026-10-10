import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "09_palindrome_number.py")

spec = importlib.util.spec_from_file_location("09_palindrome_number", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["09_palindrome_number"] = module
spec.loader.exec_module(module)

is_palindrome_num = module.is_palindrome_num


def test_palindrome_positive():
    assert is_palindrome_num(121) is True


def test_palindrome_negative():
    assert is_palindrome_num(-121) is False


def test_non_palindrome():
    assert is_palindrome_num(123) is False


def test_single_digit_palindrome():
    assert is_palindrome_num(7) is True
