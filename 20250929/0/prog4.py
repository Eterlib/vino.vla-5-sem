num = list(map(int, input().split()))

for i in num:
    if i % 2 != 0:
        print(i)
        break
else:
    print(num[0] if num else '')