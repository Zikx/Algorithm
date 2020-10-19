from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]

participant = ["leo","kiki", "eden", "leo"]
completion = ["eden", "kiki"]
participant2 = ["mislav", "stanko", "mislav", "ana","titi"]
completion2 = ["stanko", "ana", "mislav"]

print(solution(participant2,completion2))
