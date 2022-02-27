from collections import deque
n,m=map(int,input().split())
adj={i: [] for i in range(1, n+1)}
for i in range(m):
    u,v=map(int,input().split())
    adj[u].append([v,0])
    adj[v].append([u,1])
q = deque()
q.append([1, 0])
dist = [float('inf') for i in range(n+1)]
dist[1] = 0
while q:
    x,y=q.popleft()
    for i in adj[x]:
        node,dis=i
        if y+dis < dist[node]:
            if dis == 0:
                q.appendleft([node, y])
                dist[node] = y
            else:
                q.append([node, y+1])
                dist[node] = y+1

print((dist[n] if dist[n] != float('inf') else -1))
