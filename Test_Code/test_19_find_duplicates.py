import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "19_find_duplicates.py")

spec = importlib.util.spec_from_file_location("19_find_duplicates", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["19_find_duplicates"] = module
spec.loader.exec_module(module)

find_duplicates = module.find_duplicates


def test_find_duplicate_values():
    assert find_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2]


def test_no_duplicates():
    assert find_duplicates([1, 2, 3, 4]) == []


def test_all_same_values():
    assert find_duplicates([8, 8, 8]) == [8]


def test_empty_list():
    assert find_duplicates([]) == []
