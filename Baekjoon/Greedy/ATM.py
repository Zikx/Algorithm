import sys

def atm():
    num = int(sys.stdin.readline())
    withdraw_time = list(map(int, sys.stdin.readline().split()))
    result = 0
    withdraw_time.sort()

    for i in range(0,num):
        if i == 0:
            result = withdraw_time[i]
        else:
            withdraw_time[i] = withdraw_time[i - 1] + withdraw_time[i]
            result += withdraw_time[i]
    return result

print(atm())