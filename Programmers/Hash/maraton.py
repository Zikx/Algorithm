import collections

def solution(participant, completion):
    answer_counter = collections.Counter(participant) - collections.Counter(completion)
    answer = list(answer_counter.keys())[0]
    return answer


participant = ["leo","kiki", "eden"]
completion = ["eden", "kiki"]


print(solution(participant, completion))

