import sys

a, b = map(int, sys.stdin.readline().split(" "))
cnt = 1
nums = []

while len(nums) < b:
    nums.extend([cnt] * cnt)
    cnt += 1

sum_nums = sum(nums[a-1:b])

print(sum_nums)
