import sys

n = int(sys.stdin.readline())
num = 0

for i in range(n):
    tmp = i
    num = i
    for j in range(len(str(n))-1, 0, -1):
        num += tmp//(10**(j))
        tmp %= 10**j
    num += i % 10

    if num == n:
        print(i)
        break
else:
    print(0)
