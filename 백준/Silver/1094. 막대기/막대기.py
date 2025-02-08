import sys

X = int(sys.stdin.readline().strip())
result = []

while X > 0:
    result.append(X % 2)
    X //= 2

cnt = result.count(1)

print(cnt)
