from skimage import registration


def registraton(name):
    print("my name is",name)
c=registration(name)

def login(age):
    print("my age is",age)
a=login(age)

def profile(mail):
    print("my mail is",mail)
b=profile(mail)
name=input()
age=int(input())
mail=input()
d={c:name,b:age,a:mail}

print(d.items)


