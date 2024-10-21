# list는 요소 제거시 모든 요소를 한 칸씩 이동
# deque는 요소 제거시 list처럼 모든 요소를 이동하지 않음
from collections import deque

N = int(input())
arr = deque(range(1, N+1))

while (len(arr) > 1):
    arr.popleft(0)
    arr.append(arr.popleft(0))

print(arr[0])
