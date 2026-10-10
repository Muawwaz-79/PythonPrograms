import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "17_common_elements.py")

spec = importlib.util.spec_from_file_location("17_common_elements", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["17_common_elements"] = module
spec.loader.exec_module(module)

common_elements = module.common_elements


def test_common_elements_between_lists():
    assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]


def test_no_common_elements():
    assert common_elements([1, 2], [3, 4]) == []


def test_empty_list():
    assert common_elements([], [1, 2]) == []


def test_duplicates_in_input():
    assert common_elements([1, 2, 2, 3], [2, 2, 4]) == [2]
