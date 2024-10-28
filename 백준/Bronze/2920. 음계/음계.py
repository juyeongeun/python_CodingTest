num = list(map(int, input().split()))
asc_arr = sorted(num)
des_arr = sorted(num, reverse=True)

if (num == asc_arr):
    print("ascending")
elif (num == des_arr):
    print("descending")
else:
    print("mixed")
