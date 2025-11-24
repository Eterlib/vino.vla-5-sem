word = 'вопрос'

bad = word.encode('cp1251').decode('koi8-r')

print(bad)

for s in ['бМХЛЮМХЕ', 'ОХРЮМХЕ']:
    orig = s.encode('koi8-r').decode('cp1251')
    print(s, '-', orig)
