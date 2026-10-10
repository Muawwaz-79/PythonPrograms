import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "06_prime_number.py")

spec = importlib.util.spec_from_file_location("06_prime_number", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["06_prime_number"] = module
spec.loader.exec_module(module)

is_prime = module.is_prime


def test_prime_two():
    assert is_prime(2) is True


def test_prime_seven():
    assert is_prime(7) is True


def test_non_prime_four():
    assert is_prime(4) is False


def test_non_prime_one():
    assert is_prime(1) is False


def test_negative_number():
    assert is_prime(-3) is False
