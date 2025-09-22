a, b, c = map(float, input.split())

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and c + b > a:
    print('Да')
else:
    print('Нет')