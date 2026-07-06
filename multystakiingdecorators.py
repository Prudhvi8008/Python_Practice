def decor1(func):
    def inner(*args,**kwargs):
        print("func starting decor1")
        func(*args,**kwargs)
        print("func ending decor1")
    return inner
def decor2(func):
    def inner(*args,**kwargs):
        print("func starting decor2")
        func(*args,**kwargs)
        print("func ending decore2")
    return inner
@decor2
@decor1
def add(a,b):
    print("addition:",a+b)
add(10,20)