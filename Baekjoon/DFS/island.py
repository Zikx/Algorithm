# 섬의 개수
# 기본적인 그래프 순회 문제
import sys

input = sys.stdin.readline

while True:
    xandy = input()
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(y)]