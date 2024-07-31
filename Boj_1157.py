from collections import Counter

arr = input().upper()

counter = Counter(arr)

max_count = max(counter.values())

most_common = [k for k, v in counter.items() if v == max_count]

if len(most_common) > 1:
    print('?')
else:
    print(most_common[0])
