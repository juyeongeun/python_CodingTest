tc = int(input())

for _ in range(tc):
    cnt = 1
    sum = 0
    word = input()
    for i in word:
        if i == "O":
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
