import sys

tc = int(sys.stdin.readline())


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)


for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split(" "))
    print(factorial(m)//(factorial(m-n)*factorial(n)))
