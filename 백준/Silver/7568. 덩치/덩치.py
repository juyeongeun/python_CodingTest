import sys

n = int(sys.stdin.readline())

xy = []

for _ in range(n):
    xy.append(list(map(int, sys.stdin.readline().split(" "))))

for i in xy:
    rank = 1
    for j in xy:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")