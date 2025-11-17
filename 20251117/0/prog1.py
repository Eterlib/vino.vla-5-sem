def isint(f):
    def g(*a, **kw):
        for v in list(a) + list(kw.values()):
            if type(v)!=int:
                raise TypeError
        return f(*a, **kw)
    return g
