s = input().lower()

pairs = set()
for i in range(len(s)-1):
    a = s[i]
    b = s[i+1]
    if a.isalpha() and b.isalpha():
        pairs.add(a+b)

print(len(pairs))
