while True:
    s = input("Введите целое: ")
    try:
        x = int(s)
        break
    except ValueError:
        print("это не целое, попробуйте ещё раз")

print("ок, x =", x)

def itemget(coll, idx):
    return coll[idx]

def safeindex(fn, *args):
    try:
        return fn(*args)
    except IndexError:
        return None


print("safeindex 1:",
      [safeindex(itemget, "qwe", i) for i in range(5)])

try:
    print("safeindex typeerror:",
          safeindex(itemget, "qwe", "qwe"))
except TypeError as e:
    print("TypeError не пойман safeindex-ом:", e)

try:
    print("safeindex eval 1/0:",
          safeindex(eval, "1/0"))
except ZeroDivisionError as e:
    print("ZeroDivisionError тоже не ловим:", e)

def div(a, b, eps):
    if abs(b) < eps:
        raise ZeroDivisionError("слишком маленький знаменатель")
    return a / b


print("div ok:", div(10, 2, 1e-6))

try:
    print(div(10, 1e-9, 1e-6))
except ZeroDivisionError as e:
    print("div ошибка:", e)

def _wrap_as_index(fn, *args):
    try:
        return fn(*args)
    except Exception as e:
        raise IndexError("wrapped") from e


def safesafeindex(fn, *args):
    try:
        return _wrap_as_index(fn, *args)
    except IndexError as e:
        cause = e.__cause__
        if isinstance(cause, IndexError) or cause is None:
            return None
        else:
            print("NotANone:", cause)
            raise


print("safesafe index ok:",
      [safesafeindex(itemget, "qwe", i) for i in range(5)])

try:
    print("safesafe typeerror:",
          safesafeindex(itemget, "qwe", "qwe"))
except IndexError as e:
    print("поймали IndexError, cause:", repr(e.__cause__))

try:
    print("safesafe eval 1/0:",
          safesafeindex(eval, "1/0"))
except IndexError as e:
    print("eval тоже превратился в IndexError, cause:", repr(e.__cause__))
