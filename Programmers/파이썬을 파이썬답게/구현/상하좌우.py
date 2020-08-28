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

