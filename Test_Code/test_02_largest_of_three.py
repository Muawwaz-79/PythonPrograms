import importlib.util
import os
import sys

# Direct file path se program ko load karne ka tarika
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "02_largest_of_three.py")

spec = importlib.util.spec_from_file_location("02_largest_of_three", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["02_largest_of_three"] = module
spec.loader.exec_module(module)

find_largest = module.find_largest

def test_largest_numbers():
    assert find_largest(10, 5, 2) == 10
    assert find_largest(3, 15, 8) == 15
    assert find_largest(1, 4, 9) == 9

def test_equal_numbers():
    assert find_largest(5, 5, 5) == 5
    assert find_largest(7, 7, 2) == 7

def test_negative_numbers():
    assert find_largest(-1, -5, -3) == -1