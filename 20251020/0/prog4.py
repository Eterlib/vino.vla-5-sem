from collections import Counter
from timeit import Timer

def count_words_dict(text: str) -> dict:
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def count_words_counter(text: str) -> dict:
    return dict(Counter(text.split()))

text = "abc def abc qwert def abc abc qwert def abc def qwert"

t1 = Timer(lambda: count_words_dict(text))
t2 = Timer(lambda: count_words_counter(text))

print("dict:", t1.autorange())
print("Counter:", t2.autorange())

def remove_duplicates(text: str) -> str:
    return " ".join(dict.fromkeys(text.split()))
