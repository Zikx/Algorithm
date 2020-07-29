# 프로그래머스 
# Greedy level 1 체육복

def solution(n, lost, reserve):
    answer = 0
    # set = 중복을 허용하지 않는 자료형
    # list 와 비교했을 때 연산이 가능
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    print(f'set_reserve : {set_reserve}')
    
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i-1)
        elif i + 1 in set_lost:
            set_lost.remove(i+1)
    answer = n - len(set_lost)

    return answer

n = 5 
lost = [2,4]
reserve = [3]

# set 자료형은 중복 불가의 자료형 
# type = set
# 객체간의 연산 가능

print(solution(n, lost, reserve))
