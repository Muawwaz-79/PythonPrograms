import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "08_reverse_number.py")

spec = importlib.util.spec_from_file_location("08_reverse_number", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["08_reverse_number"] = module
spec.loader.exec_module(module)

reverse_number = module.reverse_number


def test_reverse_positive_number():
    assert reverse_number(1234) == 4321


def test_reverse_zero():
    assert reverse_number(0) == 0


def test_reverse_single_digit():
    assert reverse_number(9) == 9


def test_reverse_negative_number():
    assert reverse_number(-123) == -321
