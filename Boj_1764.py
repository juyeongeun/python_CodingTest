N, M = map(int, input().split())

look = set()
listen = set()

for _ in range(N):
    look.add(input())

for _ in range(M):
    listen.add(input())

result = sorted(list(look & listen))

print(len(result))
for i in result:
    print(i)
