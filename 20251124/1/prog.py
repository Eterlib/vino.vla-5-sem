import sys

data = sys.stdin.buffer.read()
if not data:
    sys.exit(0)

first_byte = data[0:1]
tail = data[1:]

if not tail:
    sys.stdout.buffer.write(data)
    sys.exit(0)

n = data[0]
L = len(tail)

parts = []
for i in range(n):
    start = int(i * L / n)
    end   = int((i + 1) * L / n)
    parts.append(tail[start:end])

parts.sort()
result_tail = b"".join(parts)

sys.stdout.buffer.write(first_byte + result_tail)
