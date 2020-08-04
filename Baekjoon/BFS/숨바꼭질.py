from collections import deque
import sys

# n = 5, k = 17
def solution(n, k):
    max_size = 100000
    visited = [-1] * (max_size+1)
    visited[n] = 0
    
    q = deque()
    q.append(n)
    cnt = 0

    while q:
        current = q.popleft()
        for nex in [current - 1, current + 1, current * 2]:
            if 0 <= nex <= max_size and visited[nex] == -1:
                q.append(nex)
                visited[nex] = visited[current] + 1
    return visited[k]


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    print(solution(n,k))






























# N,K=map(int,input().split())
# Max=10**5
# D=[-1]*(Max+1)
# D[N]=0
# q=deque()
# q.append(N)
# while q:
#     x=q.popleft()
#     for nx in [x-1,x+1,2*x]:
#         if 0<=nx<=Max and D[nx]==-1:
#             q.append(nx)
#             D[nx]=D[x]+1
# print(D[K])

#####################################################

# using back tracking 

# def solve():
#     while q:
#         cur = q.popleft()
#         if cur == k:
#             return visit[cur]
#         nextPos(cur - 1, cur)
#         nextPos(cur + 1, cur)
#         nextPos(cur * 2, cur)


# def nextPos(nex, cur):
#     # nex 지점이 범위 내에 있고
#     # 한번도 방문하지 않았거나, 최소 time으로 해당 방을 방문한 경우 
#     if (maxSize > nex >=0) and (0 == visit[nex] or visit[cur] + 1 < visit[nex]):
#         visit[nex] = visit[cur] + 1
#         q.append(nex)

# if __name__ == "__main__":
#     n, k = map(int, sys.stdin.readline().split())
#     maxSize = 100001
#     visit = [0] * maxSize
#     q = deque([n])
#     print(solve())

####################################
# using BFS

# def bfs(v):
#     count = 0        
#     q = deque([[v, count]])
#     print(q)
#     while q:
#         v = q.popleft()
#         e = v[0]
#         count = v[1]
        
#         if not visited[e]:
#             visited[e] = True
#             if e == K:
#                 return count
#             count += 1
#             if (e * 2) <= 100000:
#                 q.append([e * 2, count])
#                 print(q)
#             if (e + 1) <= 100000:
#                 q.append([e + 1, count])
#             if (e - 1) >= 0:
#                 q.append([e - 1, count])
#     return count

# N, K = map(int, sys.stdin.readline().split())
# visited = [False] * 100001
# print(bfs(N))