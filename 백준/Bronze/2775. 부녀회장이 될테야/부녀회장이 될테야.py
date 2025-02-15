import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    f = [i for i in range(1, n+1)]

    for i in range(k):
        for j in range(1, n):
            f[j] += f[j-1]

    print(f[-1])
