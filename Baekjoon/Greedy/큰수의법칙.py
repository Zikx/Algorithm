import sys 

n, m, k = map(int, sys.stdin.readline().split())

def solution(n, m, k):
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    rtn_sum = 0

    for i in range(m):
        if i % (n-1) == 0:
            rtn_sum += data[n - 2]
        else:
            rtn_sum += data[n - 1]

    return rtn_sum

print(solution(n,m,k))