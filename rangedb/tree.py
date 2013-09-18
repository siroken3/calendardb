# -*- coding: utf-8 -*-

# http://ja.wikipedia.org/wiki/%E5%8C%BA%E9%96%93%E6%9C%A8

import exception

class DegreeShouldBeEvenNumberError(excepton.Exception):
    pass

class OutofMaxIndexError(exception.Exception):
    pass

class ValueNotFoundError(exception.Exception):
    pass

class BplusTreeValue(object):
    pass

class BplusTreeNode(object):
    __slots__ = ["degree", "children", "ranges", "max_index"]

    def __init__(self, degree):
        if degree % 2 != 0:
            raise DegreeNotEvenNumberError
        self.degree = degree
        self.ranges = [None] * self.degree
        self.max_index = degree + 1
        self.children = [None] * self.max_index

    def add_child(self, index, child):
        if index > self.max_index:
            raise OutofMaxIndexError
        self.children[index] = child

class BplusTree(object):
    __slots__ = ["degree", "root"]

    def __init__(self, degree):
        self.degree = degree
        self.root = BplusTreeNode(degree)

    def add(self, a_range):
        (node, index, range) = self._find(self.root, a_range)
        # range は a_rangeを含むものが帰ってくる
        # range と a_rangeを比べて
        # range の下限が一致するが上限は小さい
        # range の上限が一致するが下限は大きい

    def delete(self, a_range):
        pass

    def find(self, a_range):
        return self._find(self.root, a_range)

    def _find(self, node, a_range):
        end_of_index = len(node.ranges) - 1
        for i, range in enumerate(node.ranges):
            if a_range < range:
                return self._find(node.children[i])
            if a_range in range:
                return (node, i, range)
            else if a_range < node.ranges[i + 1]:
                return self._find(node.children[i+1])
