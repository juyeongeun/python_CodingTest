tc = int(input())

for _ in range(tc):
    cnt, word = input().split()
    for i in range(len(word)):
        for j in range(int(cnt)):
            print(word[i], end='')
    print()
