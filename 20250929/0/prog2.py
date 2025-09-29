first = list(range(5, 16))
second = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

first[3:7] = second[-5:]

print(first)