import random
from index import BTree, BPlusTree

def test_additions():
    bt = BTree(20)
    l = range(2000)
    for i, item in enumerate(l):
        bt.insert(item)
        assert list(bt) == l[:i + 1]

def test_bulkloads():
    bt = BTree.bulkload(range(2000), 20)
    assert list(bt) == range(2000)

def test_removals():
    bt = BTree(20)
    l = range(2000)
    map(bt.insert, l)
    rand = l[:]
    random.shuffle(rand)
    while l:
        assert list(bt) == l
        rem = rand.pop()
        l.remove(rem)
        bt.remove(rem)
        assert list(bt) == l

def test_insert_regression():
    bt = BTree.bulkload(range(2000), 50)

    for i in xrange(100000):
        bt.insert(random.randrange(2000))

def test_additions_sorted():
    bt = BPlusTree(20)
    l = range(2000)

    for item in l:
        bt.insert(item, str(item))

    for item in l:
        assert str(item) == bt[item]

    assert l == list(bt)

def test_additions_random():
    bt = BPlusTree(20)
    l = range(2000)
    random.shuffle(l)

    for item in l:
        bt.insert(item, str(item))

    for item in l:
        assert str(item) == bt[item]

    assert range(2000) == list(bt)

def test_bulkload():
    bt = BPlusTree.bulkload(zip(range(2000), map(str, range(2000))), 20)

    assert list(bt) == range(2000)

    assert list(bt.iteritems()) ==  zip(range(2000), map(str, range(2000)))

