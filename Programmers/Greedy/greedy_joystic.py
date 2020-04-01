# Greedy 조이스틱 
# 65
# A B C D E F G H I J K L M 
# N O P Q R S T U V W X Y Z 'A' B C D E F G H I J K L M
# 90

def solution(name):
    answer = 0
    name = list(name)
    cp_name = ['A'] * len(name)
    cursor = 0

    while(True): 
        right=1
        left=1

        if name[cursor] != 'A':
            min_value = min(ord(name[cursor]) - ord('A'), (ord('Z') - ord(name[cursor])) + 1)
            answer += min_value
        name[cursor] = 'A'

        if name == cp_name:
            break

        for i in range(1, len(name)):
            if name[cursor + i] == "A":
                right += 1
            else:
                break
        
        for i in range(1, len(name)):
            if name[cursor - i] == "A":
                left += 1
            else:
                break
        
        if right > left:
            answer += left
            cursor -= left
        
        else:
            answer += right
            cursor += right

    return answer

print(solution("JEROEN"))