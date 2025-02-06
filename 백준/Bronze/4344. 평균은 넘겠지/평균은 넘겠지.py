C = int(input())

while (C > 0):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    cnt = 0
    for i in nums[1:]:
        if (i > avg):
            cnt += 1
    print("%.3f%%" % (cnt/nums[0] * 100))
    C -= 1
