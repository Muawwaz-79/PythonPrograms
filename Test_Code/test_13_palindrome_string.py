import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "13_palindrome_string.py")

spec = importlib.util.spec_from_file_location("13_palindrome_string", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["13_palindrome_string"] = module
spec.loader.exec_module(module)

is_palindrome_string = module.is_palindrome_string


def test_palindrome_word():
    assert is_palindrome_string("radar") is True


def test_non_palindrome_word():
    assert is_palindrome_string("python") is False


def test_empty_string():
    assert is_palindrome_string("") is True


def test_case_insensitive():
    assert is_palindrome_string("Level") is True
