import pickle

class SerCls:
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

    def __str__(self):
        return f"lst={self.lst}, dct={self.dct}, num={self.num}, st={self.st}"


ser = SerCls([1, 2, 3], {"x": 10, "y": 20}, 777, "hello")

data = pickle.dumps(ser)

del ser

ser1 = pickle.loads(data)

print("restore")
print(ser1.lst, ser1.dct, ser1.num, ser1.st)


del SerCls

class SerCls:
    def __init__(self, lst, dct, num, st):
        self.lst = lst
        self.dct = dct
        self.num = num
        self.st = st

ser2 = pickle.loads(data)

print()
print(ser2.lst, ser2.dct, ser2.num, ser2.st)


del SerCls

class SerCls:
    def __init__(self, *args):
        if args:
            self.lst, self.dct, self.num, self.st = args
        else:
            self.lst = self.dct = self.num = self.st = None

ser3 = pickle.loads(data)

print("__init__")
print(ser3.lst, ser3.dct, ser3.num, ser3.st)


del SerCls

class SerCls:
    pass

ser4 = pickle.loads(data)

print(ser4.__dict__)
