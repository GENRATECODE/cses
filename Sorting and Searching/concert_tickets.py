n,m=map(int,input().split())
h=list(map(int,input().split()))
t=list(map(int,input().split()))
h.sort()
t.sort()
for i in t:
    for j in h:
        if i<=j:
            print(i)
            h.pop(i)
        e