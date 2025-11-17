def istype(tp):
    def dec(f):
        def g(*a, **kw):
            for x in a:
                if not isinstance(x, tp):
                    raise TypeError
            for x in kw.values():
                if not isinstance(x, tp):
                    raise TypeError
            return f(*a, **kw)
        return g
    return dec
