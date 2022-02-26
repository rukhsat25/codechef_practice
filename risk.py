# cook your dish here
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def valid(x,y):
    if 0<=x<n and 0<=y<m and visited[x][y]==False and l[x][y]=="1":
        return True
    return False
def dfs(nodex,nodey):
    visited[nodex][nodey]=True
    stack=[[nodex,nodey]]
    c=1
    while stack:
        nodex,nodey=stack.pop()
        for i in range(4):
            if valid(nodex+dx[i],nodey+dy[i]):
                newx=nodex+dx[i]
                newy=nodey+dy[i]
                visited[newx][newy]=True
                c=c+1
                stack.append([newx,newy])
    return c
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        k=list(input())
        l.append(k)
    visited=[[False for i in range(m)] for j in range(n)]
    ans=[]
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False and l[i][j]=="1":
                c=dfs(i,j)
                ans.append(c)
    ans.sort(reverse=True)
    n=len(ans)
    s=0
    for i in range(n):
        if i%2:
            s=s+ans[i]
    print(s)
