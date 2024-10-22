from collections import deque
import sys

input = sys.stdin.readline

num = int(input())
arr = deque()

for _ in range(num):
    text = input()
    if "push_front" in text:
        arr.appendleft(int(text.split()[1]))
    elif "push_back" in text:
        arr.append(int(text.split()[1]))
    elif "pop_front" in text:
        if not arr:
            print(-1)
        else:
            print(arr.popleft())
    elif "pop_back" in text:
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    elif "size" in text:
        print(len(arr))
    elif "empty" in text:
        if not arr:
            print(1)
        else:
            print(0)
    elif "front" in text:
        if not arr:
            print(-1)
        else:
            print(arr[0])
    else:
        if not arr:
            print(-1)
        else:
            print(arr[-1])
