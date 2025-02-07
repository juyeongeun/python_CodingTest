import sys

N = int(sys.stdin.readline().strip())
MAX_VAL = 10**4
count = [0] * (MAX_VAL + 1)

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    count[num] += 1

for i in range(len(count)):
    if count[i]:
        for _ in range(count[i]):
            print(i)
