import sys


# 시간당 25명, 10분마다 15명 
# 1시간 = 100명, 50분 = 75명
# 하루 = 12시간
# 1일 = 1200명
# 1월 = 1024일 

# for i in range(10):

# def looping(man, l):
#     for i in l:
#         if man / i == 0:
#             print(l.index(i))
#             break
#             # return l.index(i), man
#         man = man - i
    
#     return man

wait = int(sys.stdin.readline())
man_per_day = 1200

month = [2**i for i in range(10, 0, -1)]

man_per_month = list(map(lambda x : x * man_per_day, month))

one_year = sum(man_per_month)

# year
year, wait = divmod(wait, one_year)

# month
for i in man_per_month:
    if   > wait: