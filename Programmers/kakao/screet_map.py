# def solution(n, arr1, arr2):
#     answer = []
#     for a1, a2 in zip(arr1, arr2):
#         # or 연산을 사용해서 map 의 빈공간만 확인! 
#         a12 = str(bin(a1 | a2))[2: ]
#         a12 = '0' * (n - len(a12)) + a12
#         a12 = a12.replace('1','#')
#         a12 = a12.replace('0',' ')
#         answer.append(a12)
#     return answer

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):
        a12 = str(bin(a1 | a2))[2: ]
        a12 = '0' * (n - len(a12)) + a12
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)
    
    return answer

print(solution(5, arr1, arr2))