class A:  v = 1
class B(A): v = 2

b = B(); b.v = 3
print("1) start:", b.v)

del b.v
print("1) after del b.v:", b.v)

del B.v
print("1) after del B.v:", b.v)

B.v = 2


class Vec:
    def __init__(self, x): self.x = x
    def __add__(self, other):
        return self.__class__(self.x + other.x)
    def __repr__(self): return f"{self.__class__.__name__}({self.x})"

class V2(Vec): pass

v  = Vec(10) + Vec(5)
w  = V2(10)  + V2(5)
print("2) add:", v, type(v).__name__, "|", w, type(w).__name__)


def _init_weird(self, val): setattr(self, 'Q-Q!', val)
def _str_weird(self):       return f"<Q-Q!={getattr(self,'Q-Q!')}>"

Base = type("Base", (), {'__init__': _init_weird, '__str__': _str_weird})
Child = type("Child", (Base,), {})

o1 = Base(123); o2 = Child(456)
print("3) weird:", o1, o2)

Mangled = type("Mangled", (), {"__secret": 42})
m = Mangled()
print("3b) has __secret?", hasattr(m, "__secret"), "| real name exists?", hasattr(m, "_Mangled__secret"))
# доступ вот так:
print("3b) value:", getattr(m, "_Mangled__secret"))


class P:
    def __init__(self): self.flag = "P";

class C(P):
    def __init__(self):
        super().__init__()
        self.flag += "+C"

c = C()
print("4) super init:", c.flag)


class A1:
    def __str__(self):
        chain = [cls.__name__ for cls in self.__class__.mro() if cls not in (self.__class__, object)]
        chain.append(self.__class__.__name__)
        return ":".join(chain)

class B1(A1): pass
class C1(B1): pass

print("5) A1:", str(A1()))
print("5) B1:", str(B1()))
print("5) C1:", str(C1()))
