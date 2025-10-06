def MINF(*funcs):
    def gx():
        return min(*funcs)
    return gx()

f1 = lambda x: x*5
f2 = lambda x: x*2
f3 = lambda x: x*1
f4 = lambda x: x-2

fi = [f1(3), f2(5), f3(99), f4(12)]

print(MINF(fi))