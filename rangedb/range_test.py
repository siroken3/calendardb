import range

def test_range_type3():
    r = range.Range(1,2,3)
    r.normalize()
    assert r.lower == 1
    assert r.upper == 2
    assert r.boundtype == 3

def test_range_type2():
    r = range.Range(1,2,2)
    r.normalize()
    assert r.lower == 1
    assert r.upper == 1
    assert r.boundtype == 3

def test_range_type1():
    r = range.Range(1,2,1)
    r.normalize()
    assert r.lower == 2
    assert r.upper == 2
    assert r.boundtype == 3

def test_range_type0():
    r = range.Range(1,3,0)
    r.normalize()
    assert r.lower == 2
    assert r.upper == 2
    assert r.boundtype == 3

def test_equals():
    a = range.Range(1,3,0)
    a.normalize()
    b = range.Range(2,2,3)
    assert a == b
