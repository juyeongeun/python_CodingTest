import sys

n = int(sys.stdin.readline())
num = 0

for i in range(n):
    if i+sum(map(int, str(i))) == n:
        print(i)
        break
else:
    print(0)
