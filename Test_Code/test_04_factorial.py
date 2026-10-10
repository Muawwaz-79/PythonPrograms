import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "04_factorial.py")

spec = importlib.util.spec_from_file_location("04_factorial", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["04_factorial"] = module
spec.loader.exec_module(module)

factorial = module.factorial


def test_factorial_of_zero():
    assert factorial(0) == 1


def test_factorial_of_one():
    assert factorial(1) == 1


def test_factorial_of_five():
    assert factorial(5) == 120


def test_factorial_of_seven():
    assert factorial(7) == 5040
