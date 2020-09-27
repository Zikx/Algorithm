# 1. n -= 1
# n %= k



def solution(n, k):
    cnt = 0 
    while n != 1:
        if n % k == 0:
            n //= k
            cnt += 1
        else:
            n -= 1
            cnt += 1
    return cnt

# n, k = 16, 4

print(solution(25,5))