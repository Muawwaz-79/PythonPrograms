import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "15_second_largest.py")

spec = importlib.util.spec_from_file_location("15_second_largest", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["15_second_largest"] = module
spec.loader.exec_module(module)

second_largest = module.second_largest


def test_standard_list():
    assert second_largest([12, 35, 1, 10, 34, 1]) == 34


def test_all_same_values():
    assert second_largest([5, 5, 5]) == 5


def test_small_list():
    assert second_largest([10, 20]) == 10


def test_negative_values():
    assert second_largest([-10, -20, -30, -5]) == -10
