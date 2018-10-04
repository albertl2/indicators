import pytest
from indicator import *

def test_indicator_init_no_args():
    indic = Indicator()
    assert indic.rd == [] and indic.od == []

def test_indicator_init_one_arg_num():
    indic = Indicator(31)
    assert indic.rd == [31]

def test_indicator_init_one_arg_list():
    indic = Indicator([1,2,3])
    assert indic.rd == [1,2,3]

def test_indicator_init_n_arg_num():
    indic = Indicator(1,2,3,4,3,5,7,9)
    assert indic.rd == [1,2,3,4,3,5,7,9]

def test_indicator_init_n_arg_list():
    indic = Indicator([1,2,3],[4,3],[5,7,9])
    assert indic.rd == [1,2,3,4,3,5,7,9]

def test_indicator_init_mixed_arg_list():
    indic = Indicator([1,2,3],4,3,[5,7,9])
    assert indic.rd == [1,2,3,4,3,5,7,9]

def test_indicator_update_no_args():
    indic = Indicator()
    assert indic.rd == [] and indic.od == []

def test_indicator_update_one_arg_num():
    indic = Indicator()
    indic.update(1)
    assert False

def test_indicator_update_one_arg_list():
    indic = Indicator()
    indic.update([1])
    assert False

def test_indicator_update_n_arg_num():
    indic = Indicator()
    indic.update(1,2,3,4)
    assert False

def test_indicator_update_n_arg_list():
    indic = Indicator()
    indic.update([1,2,3,4])
    assert False
