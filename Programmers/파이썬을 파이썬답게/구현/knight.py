

input_data = input()

steps = [(1,2),(-1,2),(1,-2),(-1,-2),
        (2,1),(-2,1),(2,-1),(-2,-1),]

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a') - 1)

cnt = 0 
# c,r 
for step in steps:
    if (8 >= step[0] + column > 0) and (8 >= step[1] + row > 0 ):
        cnt += 1 

print(cnt)