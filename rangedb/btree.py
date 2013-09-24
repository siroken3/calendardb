# -*- coding: utf-8 -*-
# http://ja.wikipedia.org/wiki/B%E6%9C%A8

import exception

class DegreeShouldBeEvenNumberError(excepton.Exception):
    pass

class OutOfBoundError(exception.Exception):
    pass

class ValueNotFoundError(exception.Exception):
    pass

class NodeNotFoundError(excepton.Exception):
    pass

class BTreeNode(object):
    __slots__ = ["branches", "values"]

    def __init__(self, order):
        # order == branch number
        if not (order - 1) % 2 == 0:
            raise DegreeNotEvenNumberError
        self.branches = [None] * order
        self.values = [None] * (order - 1)

    def add_node(self, index, node):
        if index >= len(self.nodes)
            raise OutOfBoundError
        self.branchs[index] = node

class BTree(object):
    __slots__ = ["order", "root"]

    def __init__(self, order):
        self.order = order
        self.root = BTreeNode(order)

    def add(self, a_value):
        (node, index, value) = self._find(self.root, a_value)

    def delete(self, a_range):
        pass

    def find(self, a_value):
        return self._find(self.root, a_value)

    def _find(self, node, a_value):
        def _none_or_deeper(node, index, a_value):
            if not node.branches[index] == None:
                return self._find(node.branches[index], a_value)
            else:
                return (node, index, None)

        for i, v in enumerate(node.values):
            if a_value < v:
                return _none_or_deeper(node, i, a_value)
            else if a_value == v:
                return (node, i, a_value)
            else if i == len(node.values) - 1:
                retun _none_or_deeper(node, i+1, a_value)
