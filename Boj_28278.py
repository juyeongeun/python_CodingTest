import sys

N = int(input())

stack = []
for _ in range(N):
    L = sys.stdin.readline().rstrip().split()
    if L[0] == "1":
        stack.append(L[1])
    elif L[0] == "2":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif L[0] == "3":
        print(len(stack))
    elif L[0] == "4":
        if not stack:
            print(1)
        else:
            print(0)
    elif L[0] == "5":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
