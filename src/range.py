# -*- coding:utf-8 -*-

import sys

class Range(object):
    # boundtype: 0:[], 1:[)
    __slots__ = ["low", "high", "boundtype"]

    @classmethod
    def empty():
        return Range(0, 0)

    def __init__(self, low=-sys.maxint - 1, high=sys.maxint, boundtype=0):
        self.low = low
        self.high = high
        self.boundtype = boundtype
        self._normalize()

    def __repr__(self):
        bound = "]" if self.boundtype == 0 else ")"
        return "[{low}, {high}{bound}".format(low=self.low, high=self.high, bound=bound)

    def _normalize(self):
        if self.boundtype == 1:
            self.high -= 1
            self.boundtype = 0

    def __eq__(self, other):
        return (self.low == other.low) and (self.high == other.high)

    def __gt__(self, other):
        if self == other:
            return False
        if self in other or other in self:
            return False
        if other.low <= self.low:
            return True
        else:
            return False

    def __ge__(self, other):
        if self == other:
            return True
        if self in other or other in self:
            return False
        if other.low <= self.low <= other.high:
            return True
        else:
            return False

    def __lt__(self, other):
        if self == other:
            return False
        if self in other or other in self:
            return False
        if self.low <= other.low:
            return True
        else:
            return False

    def __le__(self, other):
        if self == other:
            return True
        if self in other or other in self:
            return False
        if self.low <= other.low:
            return True
        else:
            return False

    def __contains__(self, other):
        if self.__eq__(other):
            return True
        if self.low <= other.low and other.high <= self.high:
            return True
        else:
            return False

    def __add__(self, other):
        if self.high == other.low or other.high == self.low:
            return Range(min(self.low, other.low), max(self.high, other.high))
        else:
            raise ValueError("{0} and {1} do not adjoin each other.".format(self, other))

    def __mul__(self, other):
        if self.low <= other.low and self.high <= other.high:
            return Range(other.low, self.high)
        if self in other:
            return self
        if other in self:
            return other
        if other.low <= self.low and other.high <= self.high:
            return Range(self.low, other.high)
        return Range(self.low, self.low)
