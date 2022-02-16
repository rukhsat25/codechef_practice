from collections import defaultdict
n,k,p=map(int,input().split())
a=list(map(int,input().split()))
l=sorted(a)
d=defaultdict(int)
x=0
d[l[0]]=x
for i in range(1,n):
    if l[i]-l[i-1]<=k:
        d[l[i]]=x
    else:
        x+=1
        d[l[i]]=x
for i in range(p):
    x,y=map(int,input().split())
    if d[a[x-1]]==d[a[y-1]]:
        print('Yes')
    else:
        print('No')
