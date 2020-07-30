# 여학생 N 
# 남학생 M 
# 참여인원 K 

# 대회 팀 = 2 * 여학생(N) + 1 * 남학생(M)

import sys 

n, m, k = map(int, sys.stdin.readline().split(" "))
t = 0

while n>=2 and m>=1 and n+m >= k+3:
    n -= 2
    m -= 1
    t += 1
print(t)
