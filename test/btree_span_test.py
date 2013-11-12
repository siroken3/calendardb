import index
from index import BTree, BPlusTree


def test_additions():
    bt = BTree(20)
    rl = [index.Span(a, a + 5) for a in range(0, 100, 5)]
    for i, r in enumerate(rl):
        bt.insert(r)
        assert list(bt) == rl[:i + 1]


def test_additions_sorted():
    bt = BPlusTree(20)
    rl = [index.Span(a, a + 5) for a in range(0, 100, 5)]

    for item in rl:
        bt.insert(item, str(item))

    for item in rl:
        assert str(item) == bt[item]

    assert rl == list(bt)


def test_contains():
    bt = BPlusTree(20)
    key_a = index.Span(1, 6)
    key_b = index.Span(6, 10)
    bt.insert(key_a, "a_value")
    bt.insert(key_b, "b_value")
    assert key_a in bt
    assert key_b in bt
    assert bt[key_a] == "a_value"
    assert bt[key_b] == "b_value"

def test_split():
    bt = BPlusTree(20)
    key_a = index.Span(1, 6)
    key_b = index.Span(3, 10)
    key_a_prime = index.Span(1, 3)
    bt.insert(key_a, "a_value")
    bt.insert(key_b, "b_value")
    assert not (key_a in bt)
    assert key_a_prime in bt
    assert key_b in bt
    assert bt[key_a_prime] == "a_value"
    assert bt[key_b] == "b_value"
