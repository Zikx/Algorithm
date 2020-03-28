import sys

def change():
    change = 1000 - int(sys.stdin.readline())
    counter = [1, 5, 10, 50, 100, 500]
    cnt = 0
    counter.reverse()

    for i in counter:
        if change >= i:
            current_cnt, change = divmod(change, i)
            cnt += current_cnt    
            
    return cnt

print(change())