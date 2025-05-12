import pytest

# def test_d():
#     print('Hai')

# def test_c():
#     a =10
#     b = 10
#     assert a == b
# def test_b():
#     a = 10
#     b = 20
#     assert a < b
# def test_a():
#     a = "arun"
#     b = "arun"
#     assert a.__eq__(b)

    #---------------------------pytest markers-----------------------#
@pytest.mark.smoke   
def test_d():
    print('Hai')
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.xfail(reason = "i wanted to check that")
def test_c():
    a =10
    b = 10
    assert a != b
@pytest.mark.skip(reason="This is an trial")
def test_b():
    a = 10
    b = 20
    assert a < b
@pytest.mark.xfail(reason = "i wanted to check that")
def test_a():
    a = "arun"
    b = "arun"
    assert a.__eq__(b)
