s = input()

vowels = set("aeiou")
letters = {ch for ch in s if 'a' <= ch <= 'z'}

v = letters & vowels
c = letters - vowels

print("гласных:", len(v), "согласных:", len(c))
