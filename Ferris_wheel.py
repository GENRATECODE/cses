n,x=map(int,input().split())
p=list(map(int,input().split()))
p.sort()
start=0
end=n-1
while start<end:
    if p[start]+p[end]<=x:
        n=n-1
        start=start+1
        end=end-1
    else:
        end=end-1
print(n)



