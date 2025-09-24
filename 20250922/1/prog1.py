n = int(input())

A = 'A +' if n % 2 == 0 and n % 25 == 0 else 'A -'
B = 'B +' if n % 2 == 1 and n % 25 == 0 else 'B -'
C = 'C +' if n % 8 == 0 else 'C -'

print(A, B, C)