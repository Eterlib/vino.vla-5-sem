import sys

name = sys.stdin.readline().strip()

try:
    with open(name, "rb") as f:
        hdr = f.read(44)
except OSError:
    print("NO")
    sys.exit(0)

if len(hdr) < 44:
    print("NO")
    sys.exit(0)

if not (hdr[0:4] == b"RIFF" and
        hdr[8:12] == b"WAVE" and
        hdr[12:16] == b"fmt " and
        hdr[36:40] == b"data"):
    print("NO")
    sys.exit(0)

size = int.from_bytes(hdr[4:8], "little")
typ = int.from_bytes(hdr[20:22], "little")
ch  = int.from_bytes(hdr[22:24], "little")
rate = int.from_bytes(hdr[24:28], "little")
bits = int.from_bytes(hdr[34:36], "little")
datasz = int.from_bytes(hdr[40:44], "little")

print(f"Size={size}, Type={typ}, Channels={ch}, Rate={rate}, Bits={bits}, Data size={datasz}")
