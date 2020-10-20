from collections import deque
from math import ceil

def solution(progresses, speeds):
    answer = []
    check = [ceil((100-x) / y) for x, y in zip(progresses, speeds)]
    
    front = 0 
    for i in range(len(check)):
        if check[front] < check[i]:
            answer.append(i - front)
            front = i
    
    answer.append(len(check) - front)
    return answer



progresses = [93, 30, 55]
speeds = [1, 30, 5]

progresses2 = [95, 90, 99, 99, 80, 99]
speeds2 = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))