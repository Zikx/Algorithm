import sys

print(max(list(map(lambda x: int(x[::-1]), sys.stdin.readline().split()))))

