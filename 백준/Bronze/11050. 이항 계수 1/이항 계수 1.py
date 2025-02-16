import sys

n, k = map(int, sys.stdin.readline().split(" "))


def factory(x):
    if x == 0 or x == 1:
        return 1
    result = x * factory(x-1)
    return result


print(factory(n) // (factory(k)*factory(n-k)))
