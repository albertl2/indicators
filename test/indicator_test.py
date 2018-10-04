import pytest
from indicator import *

# Initialization tests.
def test_indicator_init_no_args():
    indic = Indicator()
    assert indic.rd() == [] and indic.od() == []

def test_indicator_init_one_arg_num():
    indic = Indicator(31)
    assert indic.rd() == [31]

def test_indicator_init_one_arg_list():
    indic = Indicator([1,2,3])
    assert indic.rd() == [1,2,3]

def test_indicator_init_n_arg_num():
    indic = Indicator(1,2,3,4,3,5,7,9)
    assert indic.rd() == [1,2,3,4,3,5,7,9]

def test_indicator_update_no_args():
    indic = Indicator()
    assert indic.rd() == [] and indic.od() == []

def test_size_attribute_assignment():
    indic = Indicator(size=10)
    assert indic.size == 10

# Member function tests.

## Update
def test_indicator_update_one_arg_num():
    indic = Indicator()
    indic.update(1)
    assert indic.rd() == [1]

def test_indicator_update_one_arg_list():
    indic = Indicator()
    indic.update([1])
    assert indic.rd() == [1]

def test_indicator_update_n_arg_num():
    indic = Indicator()
    indic.update(1,2,3,4)
    assert indic.rd() == [1,2,3,4]

def test_indicator_update_n_arg_list():
    indic = Indicator()
    indic.update([1,2,3,4])
    assert indic.rd() == [1,2,3,4]

def test_size_attribute_array_len():
    indic = Indicator(range(11),size=10)
    assert len(indic.rd()) == 10 and len(indic.od()) == 10

# Check to see if the array recycles values correctly (FIFO).
def test_enqueue():
    indic = Indicator(size=5)
    indic.update(1,2,3,4)
    indic.update(5,6)
    assert indic.rd() == [2,3,4,5,6]
