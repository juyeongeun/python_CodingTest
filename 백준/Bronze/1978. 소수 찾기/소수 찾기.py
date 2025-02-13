import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))
cnt = 0

for i in nums:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        cnt += 1

print(cnt)
