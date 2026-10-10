import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "05_fibonacci.py")

spec = importlib.util.spec_from_file_location("05_fibonacci", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["05_fibonacci"] = module
spec.loader.exec_module(module)

fibonacci = module.fibonacci


def test_fibonacci_zero():
    assert fibonacci(0) == []


def test_fibonacci_one():
    assert fibonacci(1) == [0]


def test_fibonacci_seven():
    assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]


def test_fibonacci_ten():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
