def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        return True
def dc(n):
    dgc=0
    while n>0:
        dgc=dgc+1
        n=n//10
    return dgc
def circele(n):
    dgc=dc(n)
    r=n%10
    n=n//10
    n=(r*(10**(dgc-1)))+n
    return n
n=int(input())
dgc=dc(n)
c=0
for i in range(1,dgc+1):
    n=circele(n)
    if prime(n):
        c=c+1
if dgc==c:
    print("circlerprime")
else:
    print("not a circlerrprime")