import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "14_char_frequency.py")

spec = importlib.util.spec_from_file_location("14_char_frequency", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["14_char_frequency"] = module
spec.loader.exec_module(module)

char_frequency = module.char_frequency


def test_word_frequency():
    assert char_frequency("apple") == {"a": 1, "p": 2, "l": 1, "e": 1}


def test_repeated_letters():
    assert char_frequency("banana") == {"b": 1, "a": 3, "n": 2}


def test_empty_string():
    assert char_frequency("") == {}


def test_space_handling():
    assert char_frequency("a a") == {"a": 2, " ": 1}
