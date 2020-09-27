# 5
# R R R U D D
# 내가 접근한 방식
# import sys 

# direct = list(map(str, sys.stdin.readline().split()))
# cur_pos = [1,1]

# for i in direct: #and cur_pos[0] != 1
#     if ('L' or 'R' in i)  : # [x,]
#         if i == 'L':
#             cur_pos[0] -= 1
#             # if cur_pos[0] == 0: cur_pos = 1
#         if i == 'R':  
#             cur_pos[0] += 1# and cur_pos[1] != 1
#             print('R', i)
#     if 'U' or 'D' in i: # [,x]
#         if i == 'D':
#             cur_pos[1] -= 1
#             print('D', i)
#             # if cur_pos[1] == 0: cur_pos = 1
#         if i == 'U':  
#             cur_pos[1] += 1
#             print('U인뎅')

# print(cur_pos)

import sys

n = int(input())
x, y = 1, 1

plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x,y)