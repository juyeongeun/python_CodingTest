N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

minA = sorted(A, reverse=True)
maxB = sorted(B)

for i in range(N):
    result += minA[i]*maxB[i]

print(result)
