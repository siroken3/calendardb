import pytest
import span

def test_equals():
    a = span.Span(1,2,0)
    b = span.Span(1,3,1)
    assert a == b

def test_contains1():
    a = span.Span(1,10)
    b = span.Span(2,6)
    assert b in a
    assert not (a in b)

def test_contains2():
    a = span.Span(1,10)
    b = span.Span(1,10)
    assert a in b
    assert b in a

def test_contains3():
    a = span.Span(1,10)
    b = span.Span(2,12)
    assert not a in b
    assert not b in a

def test_ge():
    a = span.Span(1,10)
    b = span.Span(2,12)
    assert b >= a
    assert not a >= b

def test_ge2():
    a = span.Span(1,10)
    assert a >= a

def test_le():
    a = span.Span(1,10)
    b = span.Span(2,12)
    assert a <= b
    assert not b <= a

def test_le2():
    a = span.Span(1,10)
    assert a <= a

def test_gt():
    a = span.Span(1,10)
    b = span.Span(11,15)
    assert b > a
    assert not a > b
    assert not a > a

def test_lt():
    a = span.Span(1,10)
    b = span.Span(11,15)
    assert a < b
    assert not b < a
    assert not a < a

def test_add():
    a = span.Span(1,3)
    b = span.Span(2,5)
    c = span.Span(3,5)
    assert a + b == span.Span(1,5)
    with pytest.raises(ValueError):
        a + c

def test_mul():
    a = span.Span(1,3)
    b = span.Span(2,5)
    assert a * b == span.Span(2, 3)
    c = span.Span(3,5)
    assert a * c == span.Span(3, 3)

def test_split1():
    a = span.Span(1, 3)
    b = span.Span(2, 5)
    (x, y, z) = span.Span.split(a, b)
    assert x == span.Span(1, 2)
    assert y == span.Span(2, 3)
    assert z == span.Span(3, 5)

def test_split2():
    a = span.Span(1, 6)
    b = span.Span(2, 5)
    (x, y, z) = span.Span.split(a, b)
    assert x == span.Span(1, 2)
    assert y == span.Span(2, 5)
    assert z == span.Span(5, 6)

