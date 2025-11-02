from math import *

funcs = {}
defined = 1
lines = 0

def define(line):
    parts = line[1:].split()
    name = parts[0]
    params = parts[1:]
    expr = params.pop()
    funcs[name] = (params, expr)

def call(line):
    name, rest = (line.split(' ',1)+[''])[:2]

    if name=='quit':
        fmt = eval(rest) if rest else "{}:{}"
        print(fmt.format(defined, lines))
        raise SystemExit

    if name not in funcs: return
    params, expr = funcs[name]
    k = len(params)

    if k==0:
        args=[]
    elif k==1:
        args=[eval(rest)]
    else:
        args=[eval(x) for x in rest.split()]

    loc=dict(zip(params,args))

    import math
    glob = globals().copy()
    glob.update(math.__dict__)

    val = eval(expr, glob, loc)
    print(val)

while True:
    try: line=input().strip()
    except EOFError: break
    if not line: continue
    lines+=1
    if line.startswith(':'):
        define(line); defined+=1
    else:
        call(line)

import sys
exec(sys.stdin.read())