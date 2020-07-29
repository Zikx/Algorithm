import sys 

def plus_one_two(num):
    if num <= 1:
        return 1
    elif num > 3: 
        return plus_one_two(num-1) + plus_one_two(num-2)


print(plus_one_two(4))




# n = input()
# case = list() * n






# num1 = 3
# num2 = 4
# num3 = 7
# num4 = 10

