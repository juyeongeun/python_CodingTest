N = int(input())
switch = list(map(int, input().split()))
TC = int(input())

for _ in range(TC):
    gender, num = map(int, input().split())

    if gender == 1:  # 남학생인 경우
        i = num
        while i <= N:
            switch[i-1] = 1 - switch[i-1]  # 0 -> 1, 1 -> 0으로 변환
            i += num
    elif gender == 2:  # 여학생인 경우
        i = num - 1
        switch[i] = 1 - switch[i]
        left = i - 1
        right = i + 1
        while left >= 0 and right < N and switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            switch[right] = 1 - switch[right]
            left -= 1
            right += 1

for i in range(N):
    print(switch[i], end=' ')
    if (i + 1) % 20 == 0:  # 20개씩 끊어서 출력
        print()
