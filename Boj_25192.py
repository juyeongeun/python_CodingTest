num = int(input())
gom = set()
cnt = 0

for _ in range(num):
    str = input()
    if str != "ENTER":
        if str not in gom:
            cnt += 1
            gom.add(str)
    else:
        gom.clear()

print(cnt)
