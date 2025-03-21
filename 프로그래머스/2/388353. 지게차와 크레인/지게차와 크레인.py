def fork(storage, box):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    index=[]
    
    for i in range(1,len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j]==box:
                for k in range(4):
                    nx, ny = i + dx[k], j+dy[k]
                    if storage[nx][ny] == "0":
                        index.append((i,j))
                        break
                        
    for i,j in index:
        storage[i][j]="0"
        isOutside(storage,i,j)
        
def isOutside(storage, x, y):
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    outside=False
    
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if storage[nx][ny]=="0":
            storage[x][y] = "0"
            outside=True
            break
    
    if outside:
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if storage[nx][ny]=="1":
                storage[nx][ny]="0"
                isOutside(storage, nx, ny)
        

def crane(storage, box):
    for i in range(1, len(storage)-1):
        for j in range(1,len(storage[0])-1):
            if storage[i][j]==box:
                storage[i][j]="1"
                isOutside(storage, i, j)

def solution(storage, requests):
    answer=0
    storage = ["0"+i+"0" for i in storage]
    storage = [list(row) for row in storage]
    storage.insert(0, list("0" * len(storage[0])))
    storage.append(list("0" * len(storage[0])))
    
    for i in requests:
        if len(i) == 1:
            fork(storage,i)
        else:
            crane(storage,i[0])
            
    for i in range(1,len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] not in ["0", "1"]:
                answer +=1
    return answer