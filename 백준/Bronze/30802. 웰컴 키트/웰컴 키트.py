import sys

N = int(sys.stdin.readline())
T_list = list(map(int, sys.stdin.readline().split(" ")))
T, P = map(int, sys.stdin.readline().split(" "))
T_result = 0
P_result = list(map(int, (N//P, N % P)))

for i in T_list:
    if i == 0:
        continue
    if i <= T:
        T_result += 1
    elif i % T == 0:
        T_result += i // T
    else:
        T_result += (i // T) + 1

print(T_result)
print(*P_result)
