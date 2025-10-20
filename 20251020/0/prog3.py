from timeit import Timer

def count_unique_vowels_and_consonants(s: str):
    vowels = set("aeiou")
    letters = {ch for ch in s if 'a' <= ch <= 'z'}
    v = letters & vowels
    c = letters - vowels
    return len(v), len(c)

print(count_unique_vowels_and_consonants("aabABbcD123"))
t = Timer(lambda: count_unique_vowels_and_consonants("hello world"))
print("Время:", t.autorange())
