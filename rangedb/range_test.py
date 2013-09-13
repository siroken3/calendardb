import range

def test_range_type0():
    r = range.Range(1,3,0)
    assert r.low == 1
    assert r.high == 3
    assert r.boundtype == 0

def test_range_type1():
    r = range.Range(1,2,1)
    assert r.low == 1
    assert r.high == 1
    assert r.boundtype == 0

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


