s = input()
s = s[1:-1].split(',')

for i in range (len(s)):
    s[i] = int(s[i])

sor = sorted(s)
    
print(', '.join(str(i) for i in sor))


import sys
exec(sys.stdin.read())