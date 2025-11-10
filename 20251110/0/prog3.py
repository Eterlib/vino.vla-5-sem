classes = {}

class A: pass
class B: pass

class C(A, B): pass
class D(B, A): pass

classes = {'A':A, 'B':B, 'C':C, 'D':D}

ok = 0
fails = 0

for name1 in classes:
    for name2 in classes:
        pair = (classes[name1], classes[name2])

        if 'C' not in (name1, name2):
            continue

        try:
            E = type('E', pair, {})
            ok += 1
        except Exception as e:
            fails += 1

print("Успешных наследований:", ok)
print("Провальных:", fails)
