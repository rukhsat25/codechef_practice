for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[1]*n
    for j in range(1,n):
        if a[j]>=a[j-1]:
            b[j]=b[j-1]+1
    print(sum(b))
