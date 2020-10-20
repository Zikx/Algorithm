from itertools import permutations
import math



# 에라토네스 체 이용
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1)))) # 모든 경우의 수를 만듬 
#     a -= set(range(0, 2)) # 숫자 0과 1은 제거 

#     # 모든 경우의 수에 대해서 소수 판정 
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)

def check(n):
    k = math.sqrt(n)
    if n < 2: 
        return False

    for i in range(2, int(k)+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        perlist = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(perlist)):
            if check(int(i)):
                answer.append(int(i))
                print(f'te:{i}')

    answer = len(set(answer))

    return answer

print(solution("17"))