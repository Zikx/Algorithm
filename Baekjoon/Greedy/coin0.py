import sys

def coin():
    n, k = list(map(int, sys.stdin.readline().split()))
    coins = [int(sys.stdin.readline()) for i in range(n)]    
    rtn_coin_num = 0
    coins.reverse()
    for coin in coins:
        if k > 0:
            rest_of_coin, k = divmod(k, coin)
            rtn_coin_num += rest_of_coin
    
    return rtn_coin_num
