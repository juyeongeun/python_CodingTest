T=int(input())

for _ in range(T):
    arr=list(input())
    arr2=[]
    while(len(arr)):
        A=arr.pop()
        if(A==")"):
            arr2.append(A)
        elif(A=="(" and len(arr2)!=0):
            arr2.pop()
        else:
            print("NO")
            break
    else:
        if(arr2):
            print("NO")
        else:
            print("YES")