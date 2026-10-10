import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "11_vowels_consonants.py")

spec = importlib.util.spec_from_file_location("11_vowels_consonants", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["11_vowels_consonants"] = module
spec.loader.exec_module(module)

count_vowels_consonants = module.count_vowels_consonants


def test_mixed_string():
    assert count_vowels_consonants("hello world") == (3, 7)


def test_all_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert count_vowels_consonants("rhythm") == (0, 6)


def test_empty_string():
    assert count_vowels_consonants("") == (0, 0)
