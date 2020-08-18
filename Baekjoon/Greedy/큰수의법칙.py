import sys 

n, m, k = map(int, sys.stdin.readline().split())

# O(1)
# 반복되는 수열 파악

def solution(n, m, k):
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()

    max_num = data[n-1]
    second_num = data[n-2]

    count = int(m/(k+1))


# O(N)
# def solution(n, m, k):
#     data = list(map(int, sys.stdin.readline().split()))
#     data.sort()
#     rtn_sum = 0

#     for i in range(m): 
#         if i % (n-1) == 0:
#             rtn_sum += data[n - 2]
#         else:
#             rtn_sum += data[n - 1]z

#     return rtn_sum

print(solution(n,m,k))