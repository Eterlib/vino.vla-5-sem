class sole(type):
    def __new__(mcs, name, bases, attrs):
        for base in bases:
            if isinstance(base, final):
                raise TypeError(f"{base.__name__} is final")
        return type.__new__(mcs, name, bases, attrs)
