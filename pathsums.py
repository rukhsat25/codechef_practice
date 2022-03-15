from collections import deque
from collections import defaultdict

def bfs(s):
    q=deque()
    q.append(s)
    vertices[s-1]=1
    vis[s]=True
    k=2
    while q:
        x=q.popleft()
        for i in adj[x]:
            if not vis[i]:
                q.append(i)
                vis[i]=True
                if vertices[x-1]==1:
                    vertices[i-1]=2
                else:
                    vertices[i-1]=1

for i in range(int(input())):
    n=int(input())
    adj=defaultdict(list)
    for i in range(n-1):
        u,v=map(int,input().split())
        adj[u].append(v)
        adj[v].append(u)
    vis=[False for i in range(n+1)]
    vertices=[0]*n
    bfs(1)
    print(*vertices)
