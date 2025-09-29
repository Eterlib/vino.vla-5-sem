a, b = map(int, input().split())

mn, mx = min(a, b), max(a, b)

res = [n for n in range(mn, mx + 1) if n % 2 != 0 and '3' not in str(n)]
print(*res)