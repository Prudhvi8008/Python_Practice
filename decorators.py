def decor(func):
    def inner():
        print("before function")
        func()
        print(("after function"))
    return inner
@decor
def greet():
    print("decarators")
greet()



def decor2(func):
    def inner2(a,b):
        print("add")
        print("Addition result",end="")
        func(a,b)
        print("coomplete")
    return inner2
@decor2
def grret2(a,b):
    print(a+b)
grret2(10,20)


def decor3(func):
    def inner3(n):
        if n%2==0:
            print("even")

        else:
            print("odd")
        func()
    return inner3
@decor3
def grret3():
    print("number accepted")
grret3(8)




print("*"*50)
print("welcome to cvcorp \nplease enter your details \n")
username=input("enter your name: \n")
password=input("enter your password: \n")
print("registration successful")
print("*"*50)
print("enter deataials for login \n")
def decor4(func):
    def inner4():
        input1=input("enter your username: ")
        input2=input("enter your password: ")
        if input1==username and input2==password:
            print("access granted")
            func()
        else:
            print("please login first")
    return inner4
@decor4
def grret4():
    print("login successful")
    print("*"*50)
grret4()
