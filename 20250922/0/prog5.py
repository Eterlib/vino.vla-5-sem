while True:
    num = input()
    if num == '':
        break
    num = int(num)
    if num % 2 == 0:
        print(num)