import sys

N = int(sys.stdin.readline())
sum = 1
cnt = 0

for i in range(N):
    sum = sum * (i+1)


while True:
    if sum % 10 == 0:
        cnt += 1
        sum = sum // 10
    else:
        break

print(cnt)
