fn = input('file1').strip()
with open(fn, 'rb') as f:
    b = f.read(1)
    while b:
        print(b)
        b = f.read(1)