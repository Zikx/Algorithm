import sys

def solution(n,m):
    cards = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    rtn_list = []

    for i in cards:
        rtn_list.append(min(i))
    
    print(max(rtn_list))

n, m = map(int,sys.stdin.readline().split())
solution(n,m)