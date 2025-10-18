from fractions import Fraction

def parse_num(s):
    if '/' in s:
        return Fraction(s)
    else:
        return Fraction(int(s),1)

def poly_val(coeffs, x):
    res = Fraction(0,1)
    for c in reversed(coeffs):
        res = res * x + c
    return res

def check(s,w,degA,coeffsA,degB,coeffsB):
    x = parse_num(s)
    rhs = parse_num(w)
    A = poly_val(coeffsA, x)
    B = poly_val(coeffsB, x)
    if B==0: return False
    return A/B == rhs

data = input().replace(',',' ').split()
s = data[0]; w = data[1]
degA = int(data[2]); coeffsA = [parse_num(x) for x in data[3:3+degA+1]]
pos = 3+degA+1
degB = int(data[pos]); coeffsB = [parse_num(x) for x in data[pos+1:pos+1+degB+1]]

print(check(s,w,degA,coeffsA,degB,coeffsB))
