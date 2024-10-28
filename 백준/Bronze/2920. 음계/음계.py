num = list(map(int, input().split()))
asc = 0
des = 0

for i in range(7):
    if (num[i]+1 == num[i+1]):
        asc += 1
    elif (num[i]-1 == num[i+1]):
        des += 1

if (asc == 7):
    print("ascending")
elif (des == 7):
    print("descending")
else:
    print("mixed")
