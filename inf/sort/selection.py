# 선택정렬 

# 1. 주어진 리스트 중 최소값을 찾는다. 
# 2. 그 값을 맨 앞에 위치한 값과 교체한다
# 3. 맨 처음 위치를 뺀 나머지 리스트를 같은 방법으로 교체한다. 




input_value = [5, 10, 66, 77, 54, 32, 11, 15]

sorted_list = []

def selection_sort(l):
    length = len(l)
    for i in range(length - 1):
        indexMin = i
        for j in range(i+1, length):
            if l[indexMin] > l[j]:
                indexMin = j
        l[i], l[indexMin] = l[indexMin], l[i]
    return l

print(f'selection sort : {selection_sort(input_value)}')