'''My Calculator Test'''
from app.main import addition, multiplication, subtraction
def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''subtraction function'''
    assert subtraction(1,1) == 0

def test_multiplication():
    '''multiplication function'''
    assert multiplication(1,2) == 2
    