

def solution(genres, plays):
    answer = {idx : song for idx, song in enumerate(zip(genres, plays))}
    
    # rtn = sorted(answer, key=lambda x: answer[x][1], reverse=True)    
    rtn = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    return rtn


# ####
genres1 = ["classic", "pop", "classic", "classic", "pop"]
plays1 = [500, 600, 150, 800, 2500]

print(solution(genres1, plays1))

# def solution(genres, plays):
#     answer = []
#     genres_plays = {}

#     for i in range(len(plays)):
#         g = genres[i]
#         p = plays[i]
