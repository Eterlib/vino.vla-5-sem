def scale_rows(liq, new_w, new_h):
    full_liq_rows = (liq + new_w - 1) // new_w
    full_liq_rows = max(0, min(full_liq_rows, new_h))
    gas_rows = new_h - full_liq_rows
    return gas_rows, full_liq_rows

grid = []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s is None: break
    if s != "": grid.append(s)


H0 = len(grid);  W0 = len(grid[0]) if H0 else 0
inner_h = H0 - 2; inner_w = W0 - 2

liq = 0; gas = 0
for r in range(1, H0-1):
    for c in range(1, W0-1):
        ch = grid[r][c]
        if ch == '~': liq += 1
        elif ch == '.': gas += 1

total = inner_h * inner_w

new_w = inner_h
new_h = inner_w

outH = new_h + 2; outW = new_w + 2
out = [['#'] * outW for _ in range(outH)]
for r in range(1, outH-1):
    for c in range(1, outW-1):
        out[r][c] = '.'   # сначала газ

gas_rows, liq_rows = scale_rows(liq, new_w, new_h)
for rr in range(outH-2, outH-2-liq_rows, -1):
    for cc in range(1, outW-1):
        out[rr][cc] = '~'


for r in range(outH):
    print(''.join(out[r]))

barW = 20
gas_bar_len = round(barW * (gas / total)) if total else 0
liq_bar_len = round(barW * (liq / total)) if total else 0

gas_bar = '.' * gas_bar_len
liq_bar = '~' * liq_bar_len

frac_g = f"{gas}/{total}"
frac_l = f"{liq}/{total}"


max_bar = max(len(gas_bar), len(liq_bar))
max_frac = max(len(frac_g), len(frac_l))

def fmt(bar, frac):
    spaces = (max_bar - len(bar)) + 1 + (max_frac - len(frac))
    return f"{bar}{' ' * spaces}{frac}"

print(fmt(gas_bar, frac_g))
print(fmt(liq_bar, frac_l))
