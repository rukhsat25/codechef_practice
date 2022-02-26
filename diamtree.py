from collections import defaultdict
from collections import deque
def bfs(v):
    q=deque()
    vis = [0 for i in range(n+1)]
    dis = [-1 for i in range(n+1)]
    q.append(v)
    vis[v]=1
    while q:
        node=q.popleft()
        for i in tree[node]:
            if vis[i]==0:
                dis[i]=dis[node]+1
                q.append(i)
                vis[i]=1
        node,d=0,0
    for i in range(1,n+1):
        if d<dis[i]:
            d=dis[i]
            node=i
    return (node,d)
for _ in range(int(input())):
    n=int(input())
    tree=defaultdict(list)
    if n==1:
        print(0)
        continue
    for i in range(n-1):
        a,b=map(int,input().split())
        tree[a].append(b)
        tree[b].append(a)
    v1=bfs(1)
    v2=bfs(v1[0])
    print(v2[1]+1)
