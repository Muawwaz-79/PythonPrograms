import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "07_primes_in_range.py")

spec = importlib.util.spec_from_file_location("07_primes_in_range", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["07_primes_in_range"] = module
spec.loader.exec_module(module)

primes_in_range = module.primes_in_range


def test_range_with_multiple_primes():
    assert primes_in_range(10, 30) == [11, 13, 17, 19, 23, 29]


def test_range_with_small_numbers():
    assert primes_in_range(2, 10) == [2, 3, 5, 7]


def test_range_with_same_start_end():
    assert primes_in_range(7, 7) == [7]


def test_range_reversed():
    assert primes_in_range(20, 5) == []
