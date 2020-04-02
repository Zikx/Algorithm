# Programmers K번째 수 

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	

# def solution(array, commands):
#     answer = []

#     for i in range(len(commands)):
#         rtnValue = array[commands[i][0] - 1:commands[i][1]]
#         rtnValue.sort()
#         answer.append(rtnValue[commands[i][2] - 1])

#     return answer

def solution(array, commands):
    return list(map(lambda i:sorted(array[i[0] - 1 : i[1]])[i[2] - 1], commands))
    

print(solution(array, commands))