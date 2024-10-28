from collections import Counter

A = int(input())
B = int(input())
C = int(input())

answer = "".join(str(A * B * C))

result = Counter(answer)
sorted_result = dict(sorted(result.items()))

for i in range(10):
    print(sorted_result.get(str(i), 0))
