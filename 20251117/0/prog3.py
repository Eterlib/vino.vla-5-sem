class istype:
    def __init__(self, tp):
        self.tp = tp

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for v in args:
                if not isinstance(v, self.tp):
                    raise TypeError
            for v in kwargs.values():
                if not isinstance(v, self.tp):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
