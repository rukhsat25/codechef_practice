from collections import Counter
n,k=map(int,input().split())
a=list(map(int,input().split()))
c=Counter(a)
a=list(set(a))
m=(int)(10**9+7)
k=min(k,1007)
n=len(a)
dp=[[0 for i in range(k+1)] for j in range(n+1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        dp[i][j]=dp[i-1][j]+dp[i-1][j-1]*c[a[i-1]]
        dp[i][j]%=m
ans=0
for i in range(k+1):
    ans+=dp[n][i]
    ans%=m
print(ans)
