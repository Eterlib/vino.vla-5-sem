summ = 0

while True:
    num = int(input())
    if num <= 0:
        print(num)
        break
    summ += num
    if summ > 21:
        print(summ)
        break
else:
    print('Ошибка')