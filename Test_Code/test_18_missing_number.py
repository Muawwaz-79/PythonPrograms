import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "18_missing_number.py")

spec = importlib.util.spec_from_file_location("18_missing_number", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["18_missing_number"] = module
spec.loader.exec_module(module)

missing_number = module.missing_number


def test_missing_in_middle():
    assert missing_number([1, 2, 4, 5, 6]) == 3


def test_missing_first_number():
    assert missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert missing_number([1, 2, 3, 4]) == 5


def test_one_number_missing_in_larger_list():
    assert missing_number([1, 2, 3, 5, 6, 7, 8, 9, 10]) == 4
