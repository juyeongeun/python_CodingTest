import sys

n = int(sys.stdin.readline())
student = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j+1):
            if student[j][i] == student[k][i]:
                result[j][k] = 1
                result[k][j] = 1

cnt = []
for i in result:
    cnt.append(i.count(1))

print(cnt.index(max(cnt))+1)
