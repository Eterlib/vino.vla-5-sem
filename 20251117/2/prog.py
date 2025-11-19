class Num:
    def __init__(self, start_value=0):
        self._box = {}
        self._default = start_value

    def __get__(self, obj, owner=None):
        if obj is None:
            return self
        return self._box.get(id(obj), self._default)

    def __set__(self, obj, v):
        if hasattr(v, "real"):
            val = v.real
        elif hasattr(v, "__len__"):
            val = len(v)
        else:
            val = v
        self._box[id(obj)] = val

class C:
    num = Num()

import sys
exec(sys.stdin.read())