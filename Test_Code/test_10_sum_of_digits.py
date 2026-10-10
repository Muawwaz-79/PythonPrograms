import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "10_sum_of_digits.py")

spec = importlib.util.spec_from_file_location("10_sum_of_digits", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["10_sum_of_digits"] = module
spec.loader.exec_module(module)

sum_of_digits = module.sum_of_digits


def test_sum_positive_number():
    assert sum_of_digits(1234) == 10


def test_sum_zero():
    assert sum_of_digits(0) == 0


def test_sum_single_digit():
    assert sum_of_digits(7) == 7


def test_sum_negative_number():
    assert sum_of_digits(-123) == 6
