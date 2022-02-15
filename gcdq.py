import math
for _ in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    f=[0]*(n+1)
    b=[0]*(n+1)
    for i in range(1,n):
        f[i]=math.gcd(f[i-1],a[i-1])
    for i in range(n,0,-1):
        b[i-1]=math.gcd(b[i],a[i-1])
    for j in range(q):
        l,r=map(int,input().split())
        print(math.gcd(f[l-1],b[r]))
