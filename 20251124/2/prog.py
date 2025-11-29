import sys

s = sys.stdin.read()

good = s.encode('latin1', 'replace').decode('cp1251', 'replace')

sys.stdout.write(good)
