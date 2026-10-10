import importlib.util
import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(base_dir, "Code", "03_pos_neg_zero.py")

spec = importlib.util.spec_from_file_location("03_pos_neg_zero", file_path)
module = importlib.util.module_from_spec(spec)
sys.modules["03_pos_neg_zero"] = module
spec.loader.exec_module(module)

pos_neg_zero = module.pos_neg_zero


def test_positive_number():
    assert pos_neg_zero(10) == "Positive"


def test_negative_number():
    assert pos_neg_zero(-7) == "Negative"


def test_zero_number():
    assert pos_neg_zero(0) == "Zero"


def test_float_number():
    assert pos_neg_zero(3.5) == "Positive"
