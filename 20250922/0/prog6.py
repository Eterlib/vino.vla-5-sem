flag = False

while True:
    num = input()
    if num == '':
        break
    num = int(num)
    if num == 13:
        print("Обноружено число 13!")
        flag = True
        break
    if num % 2 == 0:
        print(num)

if not flag:
    print('Поздравляем, числа 13 не было!')