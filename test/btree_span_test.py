import index
from index import BTree, BPlusTree

def test_additions():
    bt = BTree(20)
    rl = [index.Span(a, a + 5) for a in range(0, 100, 5)]
    for i, r in enumerate(rl):
        bt.insert(r)
        assert list(bt) == rl[:i + 1]

def test_additions_sorted():
    bt= BPlusTree(20)
    rl = [index.Span(a, a + 5) for a in range(0, 100, 5)]

    for item in rl:
        bt.insert(item, str(item))

    for item in rl:
        assert str(item) == bt[item]

    assert rl == list(bt)

