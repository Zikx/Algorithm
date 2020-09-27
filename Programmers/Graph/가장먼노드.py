import sys 
from collections import deque


# def bfs(graph, start):
#     visited = []
#     queue = deque([start])

#     while queue:
#         n = queue.popleft()
#         if n not in visited:
#             visited.append(n)
#             queue += graph[n] - set(visited)

#     return visited


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

def dfs(graph, start):
    visited = []
    stack = list([start])

    while stack:
        n = stack.pop(0)
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print('bfs', bfs(graph, 'A'))
print('dfs', dfs(graph, 'A'))

