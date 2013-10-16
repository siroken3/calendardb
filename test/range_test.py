import pytest
import range

def test_equals():
    a = range.Range(1,2,0)
    b = range.Range(1,3,1)
    assert a == b

def test_contains1():
    a = range.Range(1,10)
    b = range.Range(2,6)
    assert b in a
    assert not (a in b)

def test_contains2():
    a = range.Range(1,10)
    b = range.Range(1,10)
    assert a in b
    assert b in a

def test_contains3():
    a = range.Range(1,10)
    b = range.Range(2,12)
    assert not a in b
    assert not b in a

def test_ge():
    a = range.Range(1,10)
    b = range.Range(2,12)
    assert b >= a
    assert not a >= b

def test_ge2():
    a = range.Range(1,10)
    assert a >= a

def test_le():
    a = range.Range(1,10)
    b = range.Range(2,12)
    assert a <= b
    assert not b <= a

def test_le2():
    a = range.Range(1,10)
    assert a <= a

def test_gt():
    a = range.Range(1,10)
    b = range.Range(11,15)
    assert b > a
    assert not a > b
    assert not a > a

def test_lt():
    a = range.Range(1,10)
    b = range.Range(11,15)
    assert a < b
    assert not b < a
    assert not a < a

def test_add():
    a = range.Range(1,2)
    b = range.Range(2,5)
    c = range.Range(3,5)
    assert a + b == range.Range(1,5)
    with pytest.raises(ValueError):
        a + c

def test_mul():
    a = range.Range(1,3)
    b = range.Range(2,5)
    assert a * b == range.Range(2, 3)
    c = range.Range(3,5)
    assert a * c == range.Range(3, 3)

def test_split1():
    a = range.Range(1, 3)
    b = range.Range(2, 5)
    (x, y, z) = range.Range.split(a, b)
    assert x == range.Range(1, 2)
    assert y == range.Range(2, 3)
    assert z == range.Range(3, 5)

def test_split2():
    a = range.Range(1, 6)
    b = range.Range(2, 5)
    (x, y, z) = range.Range.split(a, b)
    assert x == range.Range(1, 2)
    assert y == range.Range(2, 5)
    assert z == range.Range(5, 6)

