'''My Calculator Test'''
import pytest
from app.main import addition, multiplication, subtraction, division
def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''subtraction function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''multiplication function'''
    assert multiplication(1,2) == 2
def test_positive_division():
    '''positive division function'''
    assert division(1,1) == 1

def test_negative_division():
    '''negative division function'''
    with pytest.raises(ZeroDivisionError):
        division(10, 0)
