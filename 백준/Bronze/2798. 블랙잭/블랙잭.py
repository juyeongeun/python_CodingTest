import sys

n, m = map(int, sys.stdin.readline().split(" "))
num = list(map(int, sys.stdin.readline().split(" ")))
num.sort
max = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if max < num[i]+num[j]+num[k] and m >= num[i]+num[j]+num[k]:
                max = num[i]+num[j]+num[k]

print(max)
