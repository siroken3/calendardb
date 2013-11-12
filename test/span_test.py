import pytest
import index


def test_equals():
    a = index.Span(1,2)
    b = index.Span(1,2)
    assert a == b


def test_contains1():
    a = index.Span(1,10)
    b = index.Span(2,6)
    assert b in a
    assert not (a in b)


def test_contains2():
    a = index.Span(1,10)
    b = index.Span(1,10)
    assert a in b
    assert b in a


def test_contains3():
    a = index.Span(1,10)
    b = index.Span(2,12)
    assert not a in b
    assert not b in a


def test_ge():
    a = index.Span(1,10)
    b = index.Span(2,12)
    assert b >= a
    assert not a >= b


def test_ge2():
    a = index.Span(1,10)
    assert a >= a


def test_le():
    a = index.Span(1,10)
    b = index.Span(2,12)
    assert a <= b
    assert not b <= a


def test_le2():
    a = index.Span(1,10)
    assert a <= a


def test_gt():
    a = index.Span(1,10)
    b = index.Span(11,15)
    assert b > a
    assert not a > b
    assert not a > a


def test_lt():
    a = index.Span(1,10)
    b = index.Span(11,15)
    assert a < b
    assert not b < a
    assert not a < a


def test_add():
    a = index.Span(1,3)
    b = index.Span(2,5)
    c = index.Span(3,5)
    assert a + b == index.Span(1,5)
    with pytest.raises(ValueError):
        a + c


def test_mul():
    a = index.Span(1,3)
    b = index.Span(2,5)
    assert a * b == index.Span(2, 3)
    c = index.Span(3,5)
    assert a * c == index.Span(3, 3)


def test_split1():
    a = index.Span(1, 3)
    b = index.Span(2, 5)
    (x, y, z) = index.Span.split(a, b)
    assert x == index.Span(1, 2)
    assert y == index.Span(2, 3)
    assert z == index.Span(3, 5)


def test_split2():
    a = index.Span(1, 6)
    b = index.Span(2, 5)
    (x, y, z) = index.Span.split(a, b)
    assert x == index.Span(1, 2)
    assert y == index.Span(2, 5)
    assert z == index.Span(5, 6)

