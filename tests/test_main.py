'''My Calculator Test'''
from app.main import addition, subtraction
def test_addition():
    '''Addition Function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''subtraction function'''
    assert subtraction(1,1) == 0