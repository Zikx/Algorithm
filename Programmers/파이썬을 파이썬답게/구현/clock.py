
n = int(input())
cnt = 0 


for hour in range(n+1):
    for minute in range(60):
        for sec in range(60):
            if ('3' in str(hour)) or ('3' in str(minute)) or ('3' in str(sec)):
                cnt += 1

print(cnt)