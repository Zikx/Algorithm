durability = [1, 2, 1, 4]
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

# 1. jump 
# 2. weight

def cross_a_bridge(durability, dog):
    # answer = [dog[i] for i in range(len(dog))]
    answer = [i['이름'] for i in dog]

    for i in dog:
        for j in durability:
            if i['점프력'] >=
            
    return 

print(cross_a_bridge(durability, dog))