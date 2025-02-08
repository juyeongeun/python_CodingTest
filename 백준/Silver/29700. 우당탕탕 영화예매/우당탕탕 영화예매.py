import sys

N, M, K = map(int, sys.stdin.readline().split(' '))
arr = []

for i in range(N):
    arr.append(list(sys.stdin.readline().rstrip()))

result = 0

for i in range(N):
    cnt = 0
    for j in range(M):
        if arr[i][j] == '0':
            cnt += 1
        else:
            cnt = 0
        if cnt >= K:
            result += 1

print(result)
