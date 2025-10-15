from decimal import Decimal, getcontext

def esum(N, one):
    T = type(one)
    total = one
    fact = one
    for n in range(1, N+1):
        fact *= T(n)
        total += one / fact
    return total

print(esum(10, 1.0))
print(esum(20, Decimal(1)))
getcontext().prec = 50
print(esum(30, Decimal(1)))
