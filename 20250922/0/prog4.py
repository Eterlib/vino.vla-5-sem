num = 1
pravilo = 0

while True:
    chis = int(input())
    if chis == 0:
        break
    if chis == num:
        pravilo += 1
    num += 1

print(pravilo)