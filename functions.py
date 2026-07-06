#def greet(name):
 #   print(name)
#welcome=greet
#welcome("prudhvi")

##2
#num=int(input("enter a number"))
#def square(squareof):
 #   print(squareof)
#var=square
#var(num*num)

##3
#def message():
 #   print("hello python")
#msg=message
#msg()
#msg()
#msg()

##4
#count=len
#num=[10,20,30,40]
#print(count(num))


##5
#display=print
#display("functinal reference")

##6
#def applay(func,value):
 #     print(func(value))
#def cube(n):
 #     return n ** 3
#applay(cube,5)


##7
#def calclutor(a,b,operation):
 #   return operation(a,b)

#def add(a,b):
 #    return a+b

#def subtract(a,b):
 #    return a-b
#print(calclutor(3,2,add))
#print(calclutor(3,2,subtract))

##8
def is_even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
def check(num,func):
    return func(num)
func=is_even
check(5,is_even)

