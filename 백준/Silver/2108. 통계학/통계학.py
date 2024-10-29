from collections import Counter
import sys

N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

arr.sort()
counter = Counter(arr).most_common()

print(round(sum(arr) / N))

print(arr[N // 2])

if len(counter) > 1 and counter[0][1] == counter[1][1]:
    print(counter[1][0]) 
else:
    print(counter[0][0]) 

print(arr[-1] - arr[0])
