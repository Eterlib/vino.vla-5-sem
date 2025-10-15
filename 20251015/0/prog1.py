from decimal import Decimal
from fractions import Fraction

def multiplier(x, y, Type):
    return Type(x) * Type(y)

print(multiplier("1.5", "2.0", float))
print(multiplier("1.5", "2.0", Decimal))
print(multiplier("1/6", "2/3", Fraction))
