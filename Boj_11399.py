# ATM

N = int(input())
P = list(map(int, input().split()))

P.sort()
total = 0
sum = 0
for i in range(N):
    sum += P[i]
    total += sum
print(total)
