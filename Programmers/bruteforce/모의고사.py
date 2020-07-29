# 더러운코드

def solution(answers):
    re_answer = list()
    answer = [0,0,0]
    answer_len = len(answers)
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(answer_len):
        if num1[i % (len(num1))] == answers[i]:
            answer[0] += 1
        if num2[i % (len(num2))] == answers[i]:
            answer[1] += 1
        if num3[i % (len(num3))] == answers[i]:
            answer[2] += 1
    
    max_answers = max(answer)

    for i in range(len(answer)):
        if max_answers == answer[i]:
            re_answer.append(i+1)
    
    re_answer.sort()
    return re_answer

# 

answers1 = [1,2,3,4,5] # 1
answers2 = [1,3,2,4,2] # 1,2,3


print(solution(answers2))