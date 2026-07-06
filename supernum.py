def supernum(n):
    c=0
    t=n
    while n>0:
        c=c+1
        n//=10
    n=t
    sum=0
    while t>0:
        r=t%10
        sum=sum+(r**c)
        t=t//10
        c=c-1
    if sum==n:
        return True
    else:
        return False
n=int(input())
if supernum(n):
    print("supernumber")
else:
    print("not a supernumber")
