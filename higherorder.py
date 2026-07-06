def odd(n):
  #  if n%2!=0:
       # return n
 print(list(filter(odd,[1,3,4,5,6,7])))
print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7])))
def high(n):
    if n>10:
        return n
#print(list(filter(high,range(1,15))))
print(list(filter(lambda x:x>10,[1,56,45,35,8])))
print(list(filter(lambda x:x%5==0,[1,2,3,35,45,46,75,60])))
print(list(filter(lambda x:x in ["a","e","i","o","u"],"prudhvi")))
print(list(filter(lambda x:x not in "aeiouAEIOU" ,"prUdhvi")))
def check(n):
    if n<0:
        return n
print(list(filter(check,[1,2,3,4,-4,-9,-4])))

from functools import reduce
def summ(x,y):
    return x+y
print(reduce(summ,[1,2,3,4,-4,-9,-5]))
print(reduce(lambda x,y:x*y,[1,2,3,4,5,6,7,8,9]))
print(reduce(lambda x,y:x if len(x)>len(y) else y,["prudhvi","manikanta","siva","sandeep"] ))
print(reduce(lambda x,y:x+y,["prudhvi","manikanta","siva","sandeep"] ))
a=[1,2,3,4,5,6,7,8,9]
print(reduce(lambda c,x: c+1 if x%2==0 else c,a,0))
print(reduce(lambda sum,x: sum+x*x ,a,0))


