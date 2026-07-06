from functools import reduce
s=["tea","biscuits","chocolate","bread","ice-cream","coffee"]
print(reduce(lambda x,y:x+y,(sorted(list(filter(lambda x:(x%3==0)^(x%5==0),list(map(lambda x:len(x)+5,s)))),reverse=True))))
