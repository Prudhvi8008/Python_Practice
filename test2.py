def order(product,quantity=1,price=0):
    print("product is",product)
    print("quantit is",quantity)
    print("price is",price)
order("pizza")
order("pizza",4,400)
order(product="pizza",quantity=2,price=200)

#2
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def math_oper(a,b,operation):
    return operation(a,b)
print(math_oper(3,1,add))
print(math_oper(3,1,sub))

#3
a=0
b=(lambda a:"positive" if a>0 else ("negative" if a<0 else "zero"))
print(b(a))


def calculator(a,b,operation):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    def div():
        return a/b
    def mod():
        return a%b
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
calculator(2,1,"+")
calculator(2,1,"-")
calculator(2,1,"*")
calculator(2,1,"/")
calculator(2,1,"%")
