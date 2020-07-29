# a : 고정비용
# b : 한대의 노트북을 생산하는 비용 
# c : 노트북의 가격
# a + (b * x) < (c * x)
# x를 구할 것.

# 노트북 생산비용이 노트북 가격보다 클리가 없으니까 먼저 걸러주고 
# 그 후에 이익을 계산 
# 이익부터 계산하면 런타임에러 ㅠㅠ

import sys
def break_even_point(a,b,c):
    if c <= b :
        return -1
    else:
        return a // (c - b) + 1

fixed_price, var_price, laptop = map(int, sys.stdin.readline().split(" "))
print(break_even_point(fixed_price,var_price,laptop))