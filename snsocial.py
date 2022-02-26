from collections import deque
dir=[[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[1,-1],[-1,1]]
def get_max(grid):
    m=0
    for i in grid:
        for j in i:
            m=max(m,j)
    return m

def valid(i,j):
    if i<0 or j<0 or i>=n or j>=m:
        return 0
    return 1

for _ in range(int(input())):
    n,m=map(int,input().split())
    grid=[]
    vis = [[0 for _ in range(m)] for __ in range(n)]
    dis=[[0 for _ in range(m)] for __ in range(n)]

    for i in range(n):
        grid.append(list(map(int,input().split())))
    maxi=get_max(grid)


    q=deque()
    for i in range(n):
        for j in range(m):
            if grid[i][j]==maxi:
                q.append([i,j])
                vis[i][j]=1
    
    ans=0
    while(q):
        x,y=q.popleft()
        for i in dir:
            X,Y=x+i[0],y+i[1]
            if valid(X,Y) and vis[X][Y]==0:
                q.append([X,Y])
                vis[X][Y]=1
                dis[X][Y]=dis[x][y]+1
                ans=max(dis[X][Y],ans)
    
    print(ans)
