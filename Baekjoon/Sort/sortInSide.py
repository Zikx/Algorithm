nums = input()

number = [int(n) for n in nums]

sort_nums = sorted(nums, reverse=True)

for n in sort_nums :
    print(n, end="")