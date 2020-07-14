# 삽입정렬 

input_list = [5, 10, 66, 77, 54, 32, 11, 15]

sorted_list = []

def insert_index(l, insert_value):
    for i in range(len(l)):
        if insert_value < l[i]: 
            return i
    return len(l)

while input_list:
    insert_value = input_list.pop(0)
    idx = insert_index(sorted_list, insert_value)
    sorted_list.insert(idx, insert_value)

print(sorted_list)