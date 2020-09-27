from collections import deque
import sys 

# dfs -> stack 
# bfs -> queue
# v => root

# def DFS(root, graph):
#     l = list([root])


n, m, v = map(int, sys.stdin.readline().split())

for _ in range(m):
    graph = []
    graph.append(list(map(int, sys.stdin.readline().split())))

print(graph)