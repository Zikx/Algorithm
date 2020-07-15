# import collections

# def solution(participant, completion):
#     answer_counter = collections.Counter(participant) - collections.Counter(completion)
#     answer = list(answer_counter.keys())[0]
#     return answer


# participant = ["leo","kiki", "eden"]
# completion = ["eden", "kiki"]


# print(solution(participant, completion))

participant = ["leo","kiki", "eden"]
completion = ["eden", "kiki"]

participant2 = ["mislav", "stanko", "mislav", "ana"]
completion2 = ["stanko", "ana", "mislav"]

from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]

print(solution(participant2, completion2))
