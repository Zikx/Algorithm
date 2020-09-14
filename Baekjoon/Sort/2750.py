n = int(input())
l = [ int(input()) for i in range(n)]
l.sort()

for e in l:
    print(e,end="\n")   