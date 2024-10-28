num = list(map(int, input().split()))
asc = 0
des = 0
asc_arr = sorted(num)
des_arr = sorted(num, reverse=True)

if (num == asc_arr):
    print("ascending")
elif (num == des_arr):
    print("descending")
else:
    print("mixed")
