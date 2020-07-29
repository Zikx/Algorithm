from collections import Counter

def solution(clothes):
    category_clothes = Counter([category for name, category in clothes])
    cnt = 1
    for values in category_clothes.values():
        cnt *= values + 1

    return cnt - 1


clothes1 = [["yellow_hat", "headgear"], 
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"]]

clothes2 = [["crow_mask", "face"], 
            ["blue_sunglasses", "face"], 
            ["smoky_makeup", "face"]]


# print(solution(clothes1)) # return 5
print(solution(clothes2)) # return 3








