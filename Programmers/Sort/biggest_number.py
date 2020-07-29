# Rule 1 
# - 가장 큰 수를 구할것, 
# i < 10 => (i % 10).sort()
# i >= 10 => (i / 10)

mylist = ['1','2','3']
def solution(mylist):
    return list(map(int, mylist))

print(solution(mylist))

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x * 3, reverse = True)
#     if sum(list(map(int, numbers))) == 0:
#         numbers = list(set(numbers))
    
#     return ''.join(numbers)

# numbers1 = [6, 10, 2, 2]
# numbers2 = [3, 30, 34, 5, 9]

# print(solution(numbers1))

# import itertools

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
