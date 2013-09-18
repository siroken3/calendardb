# -*- coding:utf-8 -*-

import sys

class Range(object):
    # boundtype: 0:[], 1:[)
    __slots__ = ["low", "high", "boundtype"]

    def __init__(self, low=-sys.maxint - 1, high=sys.maxint, boundtype=1):
        self.low = low
        self.high = high
        self.boundtype = boundtype
        self._normalize()

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
        if self.low <= other.low and self.high >= other.high:
            return True
        else:
            return False

