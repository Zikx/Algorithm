import sys

e1, e2 = map(int, sys.stdin.readline().split(" "))

if e2 < 45 and e1 == 0: 
    e1 = 24
h1, m1 = divmod((e1 * 60 + e2) - 45, 60)

print(h1, m1)