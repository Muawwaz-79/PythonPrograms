import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "20_word_frequency.py")

spec = importlib.util.spec_from_file_location("20_word_frequency", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["20_word_frequency"] = module
spec.loader.exec_module(module)

word_frequency = module.word_frequency


def test_word_frequency_sentence():
    assert word_frequency("hello world hello") == {"hello": 2, "world": 1}


def test_empty_sentence():
    assert word_frequency("") == {}


def test_single_word():
    assert word_frequency("python") == {"python": 1}


def test_multiple_repeated_words():
    assert word_frequency("one two one two one") == {"one": 3, "two": 2}
