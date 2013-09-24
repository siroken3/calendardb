# -*- coding: utf-8 -*-

# http://ja.wikipedia.org/wiki/%E5%8C%BA%E9%96%93%E6%9C%A8

import exception

class DegreeShouldBeEvenNumberError(excepton.Exception):
    pass

class OutofMaxIndexError(exception.Exception):
    pass

class ValueNotFoundError(exception.Exception):
    pass

class NodeNotFoundError(excepton.Exception):
    pass

class BTreeNode(object):
    __slots__ = ["children", "ranges", "max_index"]

    def __init__(self, degree):
        if degree % 2 != 0:
            raise DegreeNotEvenNumberError
        self.ranges = [None] * self.degree
        self.max_index = degree + 1
        self.children = [None] * self.max_index

    def add_child(self, index, child):
        if index > self.max_index:
            raise OutofMaxIndexError
        self.children[index] = child

class BTree(object):
    __slots__ = ["degree", "root"]

    def __init__(self, degree):
        self.degree = degree
        self.root = BTreeNode(degree)

    def add(self, a_range):
        (node, index, range) = self._find(self.root, a_range)

    def delete(self, a_range):
        pass

    def find(self, a_range):
        return self._find(self.root, a_range)

    def _find(self, node, a_range):
        end_of_index = len(node.ranges) - 1
        for i, r in enumerate(node.ranges):
            if a_range < r:
                return self._find(node.children[i], a_range)
            if a_range in r:
                return (node, i, r)
            else if a_range < node.ranges[i + 1]:
                return self._find(node.children[i+1], a_range)
