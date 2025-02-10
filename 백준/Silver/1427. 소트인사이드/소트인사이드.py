import sys

n = list(map(str, sys.stdin.readline().rstrip()))
print("".join(sorted(n, reverse=True)))
