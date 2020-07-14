def solution(heights):
    answer = [0] * len(heights)

    while heights:
        element = heights.pop()
        for e in range(len(heights) - 1, -1, -1):
            if element < heights[e]:
                answer[len(heights)] = e + 1
                break

    return answer



heights1 = [3,9,9,3,5,7,2] # 0,0,2,2,4
heights2 = [6,9,5,7,4] # 0,0,0,3,3,3,6
heights3 = [1,5,3,6,7,6,5] # 0,0,2,0,0,5,6

print(solution(heights2))
