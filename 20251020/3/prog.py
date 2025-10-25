import re
from collections import Counter

w = int(input())
lines = []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s == "": break
    lines.append(s)

txt = " ".join(lines).lower()
txt = re.sub(r'[^a-z]', ' ', txt)

words = [t for t in txt.split() if len(t)==w]
if words:
    cnt = Counter(words)
    m = max(cnt.values())
    top = [k for k,v in cnt.items() if v==m]
    top.sort()
    print(" ".join(top))
