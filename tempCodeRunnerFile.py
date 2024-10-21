N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in range(N):
    if B[i] not in A:
        print(0)
    else:
        print(1)
