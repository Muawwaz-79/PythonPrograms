import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "12_reverse_string.py")

spec = importlib.util.spec_from_file_location("12_reverse_string", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["12_reverse_string"] = module
spec.loader.exec_module(module)

reverse_string = module.reverse_string


def test_reverse_word():
    assert reverse_string("python") == "nohtyp"


def test_reverse_sentence():
    assert reverse_string("hello world") == "dlrow olleh"


def test_empty_string():
    assert reverse_string("") == ""


def test_single_character():
    assert reverse_string("a") == "a"
