#1
a=["a","b","@","A"]
print(list(map(lambda x:ord(x),a)))
#2
b=[[1,3],[4,5],[6,7]]
print(list(map(lambda x:list(map(lambda y:y+5,x)),b)))
#3
n=[12,15,7,18,20,21,25]
print(list(filter(lambda x: (x%3)^(x%5),n)))
#4
print(list(filter(lambda x:x.lower() not in "aeiou","prudhvi")))
#5
from functools import reduce
s=['p','y','t','h','o','n']
print(reduce(lambda x,y:x+y,s))
#6
from functools import reduce
a=[5,10,15,20,25,30]
print(reduce(lambda x,y:x+y,(sorted(list(filter(lambda x:x%5==0,list(map(lambda x:x**2,a)))),reverse=True))))