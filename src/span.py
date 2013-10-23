# -*- coding:utf-8 -*-

import sys

class Span(object):
    # boundtype: 0:[], 1:[)
    __slots__ = ["low", "high", "boundtype"]

    @classmethod
    def empty(cls):
        return Span(0, 0)

    @classmethod
    def split(cls, range_a, range_b):
        center = range_a * range_b
        left = cls(min(range_a.low, range_b.low), center.low)
        right = cls(center.high, max(range_a.high, range_b.high))
        return (left, center, right)

    def __init__(
            self,
            low=-sys.maxint-1,
            high=sys.maxint,
            boundtype=1):
        self.low = low
        self.high = high
        self.boundtype = boundtype
        self._normalize()

    def __repr__(self):
        bound = "]" if self.boundtype == 0 else ")"
        return "[{low}, {high}{bound}".format(
            low=self.low, high=self.high, bound=bound)

    def _normalize(self):
        if self.boundtype == 1:
            self.high -= 1
            self.boundtype = 0

    def __eq__(self, other):
        return (self.low == other.low) and (self.high == other.high)

    def __contains__(self, other):
        if self == other:
            return True
        if self.low <= other.low and other.high <= self.high:
            return True
        return False

    def __gt__(self, other):
        if self in other or other in self:
            return False
        if other.low <= self.low:
            return True
        return False

    def __ge__(self, other):
        return (self == other) or (self > other)

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return (self == other) or (self < other)

    def __add__(self, other):
        if self.high == other.low or other.high == self.low:
            return Span(min(self.low, other.low), max(self.high, other.high))
        else:
            raise ValueError(
                "{0} and {1} do not adjoin each other.".format(self, other))

    def __mul__(self, other):
        if self.low <= other.low and self.high <= other.high:
            return Span(other.low, self.high)
        if self in other:
            return self
        if other in self:
            return other
        if other.low <= self.low and other.high <= self.high:
            return Span(self.low, other.high)
        return Span(self.low, self.low)
