import itertools

n = 3
nums = range(1, 20)

res = itertools.filterfalse(lambda x: x % n == 0, nums)
print(list(res))
