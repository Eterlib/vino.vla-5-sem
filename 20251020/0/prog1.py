import timeit

snippet = input()
t = timeit.Timer(stmt=snippet)
num, total = t.autorange()
avg = total / num

print(f"{avg:.6f} sec per loop (mean of {num} runs)")
