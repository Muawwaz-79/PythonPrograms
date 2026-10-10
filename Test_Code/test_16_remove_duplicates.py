import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "16_remove_duplicates.py")

spec = importlib.util.spec_from_file_location("16_remove_duplicates", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["16_remove_duplicates"] = module
spec.loader.exec_module(module)

remove_duplicates = module.remove_duplicates


def test_remove_duplicates_from_list():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_single_value_list():
    assert remove_duplicates([7]) == [7]


def test_order_preserved():
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
