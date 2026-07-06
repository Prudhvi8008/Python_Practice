def calculator(*a,operation):
    def reslut():
        def add():
            return add(lambda x,y:x+y,*a)
        def sub():
            return a-b
        def mul():
            return a*b
        def div():
            return a/b
        def mod():
            return a%b
        def flor():
            return a//b


        if operation=="+":
            print(add())
        elif operation=="-":
            print(sub())
        elif operation=="*":
            print(mul())
        elif operation=="/":
            print(div())
        elif operation=="%":
            print(mod())
        elif operation=="//":
            print(flor())
    reslut()
a=int(input())
b=int(input())
operation=input()
calculator(a,b,operation)
#calculator(3,1,"+")
#calculator(3,1,"-")
#calculator(3,1,"*")
#calculator(3,1,"/")
#calculator(3,1,"%")
#calculator(3,1,"//")
