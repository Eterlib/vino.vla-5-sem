from collections import Counter

article = input().split()
note = input().split()

c_article = Counter(article)
c_note = Counter(note)

if c_note - c_article == Counter():
    print("YES")
else:
    print("NO")
