num = int(input())

match num:
    case 1:
        print('один')
    case 2:
        print('два')
    case 3:
        print('три')
    case _:
        if num % 2 == 0:
            print('четное')
        else:
            print(f'{num} -- это много')