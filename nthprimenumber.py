def nthprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    return False
n=int(input())
dc=0
i=0
while True:
    if nthprime(i):
        dc=dc+1
    if dc==n:
        print(i)
        break
    i=i+1
