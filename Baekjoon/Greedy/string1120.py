import sys

def string1120():
    a, b = list(map(str, sys.stdin.readline().split()))
    Min = 50

    for i in range(len(b) - len(a) + 1):
        cnt = 0 
        for j in range(len(a)):
            if a[j] != b[i+j]:
                cnt += 1
        if cnt<Min:
            Min = cnt
    return Min

print(string1120())