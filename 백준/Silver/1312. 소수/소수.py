import sys

n, m, k = map(int, sys.stdin.readline().split(" "))

for _ in range(k):
    n = (n % m)*10
    result = n//m

print(result)
