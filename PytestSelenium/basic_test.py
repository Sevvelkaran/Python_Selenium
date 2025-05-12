import pytest

def test_sample_one():
    print('Hai')

def test_sample_two():
    a =10
    b = 10
    assert a == b
def test_sample_three():
    a = 10
    b = 20
    assert a < b
def test_sample_four():
    a = "arun"
    b = "aruns"
    assert a.__eq__(b)