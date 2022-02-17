n=100001
p=[0]*n
for i in range(2,n):
    if p[i]==0:
        for j in range(i,n,i):
            p[j]+=1
ans=[[0,0,0,0,0,0] for i in range(n)]
for i in range(n):
    if p[i]<6 :
        ans[i][p[i]]+=1
for i in range(n):
    for j in range(6):
        ans[i][j]+=ans[i-1][j]
for _ in range(int(input())):
    a,b,k=map(int,input().split())
    print(ans[b][k]-ans[a-1][k])
