from collections import UserString


class DivStr(UserString):
    def __init__(self, s=""):
        super().__init__(s)

    def __floordiv__(self, n):
        l = len(self.data)
        size = l // n
        def gen():
            for i in range(n):
                start = i * size
                end = start + size
                yield DivStr(self.data[start:end])
        return gen()

    def __mod__(self, n):
        l = len(self.data)
        r = l % n
        if r == 0:
            return DivStr()
        return DivStr(self.data[-r:])

    def lower(self):
        return DivStr(self.data.lower())

    def __getitem__(self, key):
        res = self.data[key]
        if isinstance(key, slice):
            return DivStr(res)
        return res

import sys
exec(sys.stdin.read())