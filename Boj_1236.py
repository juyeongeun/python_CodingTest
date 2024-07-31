n, m = map(int, input().split())

castle = [input().strip() for _ in range(n)]

row_guard_needed = 0
col_guard_needed = 0

for i in range(n):
    if 'X' not in castle[i]:
        row_guard_needed += 1

for j in range(m):
    if 'X' not in [castle[i][j] for i in range(n)]:
        col_guard_needed += 1

print(max(row_guard_needed, col_guard_needed))
