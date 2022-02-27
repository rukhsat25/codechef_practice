for _ in range(int(input())):
    n=int(input())
    l=[0]*(n+1)
    for i in range(n-1):
        u,v=map(int,input().split())
        l[v]+=1
    c=0
    for i in l:
        if i==0:
            c+=1
    print(c-2)
