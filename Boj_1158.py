N, K = map(int, input().split())

arr = [i for i in range(1, N+1)]
cnt = 0
answer = []

while (arr):
    cnt += K-1
    if (cnt >= len(arr)):
        cnt = cnt % len(arr)

    answer.append(arr.pop(cnt))

print('<' + ', '.join(str(i) for i in answer) + '>')
