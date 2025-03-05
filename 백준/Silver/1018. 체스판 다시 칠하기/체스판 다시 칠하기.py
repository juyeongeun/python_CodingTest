import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = []
cnt = []

for i in range(n):
    arr.append(sys.stdin.readline())

for i in range(n-7):
    for j in range(m-7):
        black = 0
        white = 0

        for k in range(i, i+8):
            for q in range(j, j+8):
                if (k+q) % 2 == 0:
                    if arr[k][q] == 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if arr[k][q] == 'B':
                        white += 1
                    else:
                        black += 1

        cnt.append(black)
        cnt.append(white)

print(min(cnt))
