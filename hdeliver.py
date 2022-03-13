from collections import deque
from collections import defaultdict

def bfs(s,k):
    q=deque()
    q.append(s)
    compo[s]=k
    vis[s]=True
    while q:
        x=q.popleft()
        for i in adj[x]:
            if not vis[i]:
                q.append(i)
                compo[i]=k
                vis[i]=True
    

for i in range(int(input())):
    n,m=map(int,input().split())
    adj=defaultdict(list)
    for i in range(m):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    vis=[False for i in range(n)]
    compo=[-1]*n
    k=0
    for i in range(n):
        if not vis[i]:
            bfs(i,k)
            k+=1
    q=int(input())
    for i in range(q):
        a,b=map(int,input().split())
        if compo[a]==compo[b]:
            print('YO')
        else:
            print('NO')
