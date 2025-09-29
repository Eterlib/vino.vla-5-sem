num = input().split()

num2 = num[len(num)//2:]
pick = num2[0::2]
res = pick[::-1]

print(res) # можно вывести *res, так красивее