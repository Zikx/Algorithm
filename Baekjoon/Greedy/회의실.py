import sys

n = int(input())

timeline = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
timeline.sort(key=lambda x: -(x[1] - x[0]))
cnt = 0


# for i in timeline:

print(timeline) 