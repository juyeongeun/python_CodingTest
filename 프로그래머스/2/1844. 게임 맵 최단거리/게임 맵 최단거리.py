from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx, dy = [0,0,1,-1], [1,-1,0,0]
    queue=deque()
    queue.append((0,0))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if  nx < n and ny < m and nx>=0 and ny>=0 and maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y] +1
                queue.append((nx,ny))
    
    if maps[n-1][m-1]>1:
        return maps[n-1][m-1]
    else:
        return -1
        