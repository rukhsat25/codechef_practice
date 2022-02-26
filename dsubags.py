class DSU:
    def __init__(self,maxsize):
        self.currsize = maxsize
        self.parent = [-1]*(maxsize+1)
    
    def root(self,u):
        if(self.parent[u]==-1):
            return u
        else:
            self.parent[u] = self.root(self.parent[u])
            return self.parent[u]
    
    def union(self,u,v):
        u,v = self.root(u),self.root(v)
        if(u==v):
            pass
        else:
            self.parent[v] = u
            self.currsize-=1
    
    def find(self,u,v):
        return (self.root(u)==self.root(v))
    
    def size(self):
        return self.currsize

n,queries = map(int,input().split())
D = DSU(n)
for query in range(0,queries):
    A = [int(i) for i in input().split()]
    if(A[0]==1):
        D.union(A[1],A[2])
    elif(A[0]==2):
        print("YES" if(D.find(A[1],A[2])) else "NO")
    else:
        print(D.size())
