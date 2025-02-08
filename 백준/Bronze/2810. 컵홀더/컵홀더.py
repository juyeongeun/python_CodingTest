import sys

N = int(sys.stdin.readline().strip())
result = 1
cnt = 1

seat = list(sys.stdin.readline().strip())

for i in seat:
    if i == "S":
        result += 1
    else:
        if cnt == 1:
            cnt += 1
        else:
            cnt = 1
            result += 1

print(min(result, N))
