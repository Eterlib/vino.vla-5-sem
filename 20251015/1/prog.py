from fractions import Fraction

def to_frac(v):
    if isinstance(v, Fraction): return v
    if isinstance(v, (int, float)): return Fraction(v).limit_denominator()
    v = v.strip()
    return Fraction(v)

def poly_val(coeffs, x):
    res = Fraction(0, 1)
    for c in coeffs:
        res = res * x + c
    return res

def check(s, w, degA, coeffsA, degB, coeffsB):
    x = to_frac(s)
    rhs = to_frac(w)
    A = poly_val(coeffsA, x)
    B = poly_val(coeffsB, x)
    if B == 0:
        return False
    return A / B == rhs

tokens = input().replace(',', ' ').split()

s, w = tokens[0], tokens[1]

degA = int(tokens[2])
a_start = 3
a_end = a_start + degA + 1
coeffsA = [to_frac(t) for t in tokens[a_start:a_end]]

degB = int(tokens[a_end])
b_start = a_end + 1
b_end = b_start + degB + 1
coeffsB = [to_frac(t) for t in tokens[b_start:b_end]]

print(check(s, w, degA, coeffsA, degB, coeffsB))
