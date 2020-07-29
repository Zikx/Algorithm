dog = [{
    "이름" : "루비독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "4",
    },{
    "이름" : "피치독",
    "나이" : "95년생",
    "점프력" : "3",
    "몸무게" : "3",
    },{
    "이름" : "씨-독",
    "나이" : "72년생",
    "점프력" : "2",
    "몸무게" : "1",
    },{
    "이름" : "코볼독",
    "나이" : "59년생",
    "점프력" : "1",
    "몸무게" : "1",
    }
]
durability1 = [1, 2, 1, 4]
durability2 = [10, 20, 10, 40, 10, 10, 10]

# 1. jump 
# 2. weight

# remove O(N)
# del O(1)

# def cross_a_bridge(durability, dog):
#     answer = [i['이름'] for i in dog]
    
#     for i in dog:
#         where_dog = 0
#         while where_dog < len(durability) - 1:
#             where_dog += int(i['점프력'])
#             durability[where_dog - 1] -= int(i['몸무게'])
#             if durability[where_dog - 1] < 0:
#                 del answer[answer.index(i['이름'])]
#                 break
#     return answer

# print(cross_a_bridge(durability1.copy(), dog.copy()))

import json

json_dog = json.dumps(dog, ensure_ascii=False)
# print(json_dog) # 문자열 

# json.loads(json객체) 로 json 처리할 것
json_dog = json.loads(json_dog)
print(json_dog[0])