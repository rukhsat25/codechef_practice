from collections import defaultdict
from collections import deque
n,m=map(int,input().split())
adj=defaultdict(list)
q=deque()
def bfs(v):
    s=[v]
    q.append(v)
    vis[v]=1
    while q:
        node =q.popleft()
        for i in adj[node]:
            if vis[i]==0:
                q.append(i)
                vis[i]=1
                s.append(i)
    return s

for i in range(m):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
price=[0]
vis=[0]*(n+1)
for i in range(n):
    price.append(int(input()))
components=[]
for i in range(1,n+1):
    if vis[i]==0:
        components.append(bfs(i))

#print(components)
ans=[]
f=0
if len(components)==1:
    print(0)
else:
    for i in components:
        a=float('inf')
        for j in i:
            if price[j]>=0:
                a=min(a,price[j])
        if a==float('inf'):
            f=1
            break
        ans.append(a)
    if f==0:
        print(sum(ans)+min(ans)*(len(components)-2))
    else:
        print(-1)
