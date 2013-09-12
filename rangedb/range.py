# -*- code:utf-8 -*-

import sys

class Range(object):
    # boundtype: 0:(), 1:(], 2:[), 3:[]
    __slots__ = ["lower","upper", "boundtype"]

    def __init__(self, lower=-sys.maxint - 1, upper=sys.maxint, boundtype=3):
        self.lower = lower
        self.upper = upper
        self.boundtype = boundtype

    def normalize(self):
        if self.boundtype == 0:
            self.lower += 1
            self.upper -= 1
            self.boundtype = 3
        if self.boundtype == 1:
            self.lower += 1
            self.boundtype = 3
        if self.boundtype == 2:
            self.upper -= 1
            self.boundtype = 3

    def __eq__(self, other):
        other.normalize()
        return (self.lower == other.lower) and (self.upper == other.upper)


