def login_required(func):
    def inner():
        print("checking login")
        func()
    return inner
def admin_required(func):
    def inner():
        print("checking admin permission")
        func()
    return inner
@login_required
@admin_required
def delete_required():
    print("Recoed deleted")
delete_required()


def  decor1(func):
    def inner(*args,**kwargs):
        print("before calculation")
        func(*args,**kwargs)
        print("after calculation")
    return inner
def decor2(func):
    def inner(*args,**kwargs):
        print("cheking inputs")
        func(*args,**kwargs)
    return inner
@decor1
@decor2
def validate(a,b):
    print(a+b)
validate(10,20)

def auth_required(func):
    def inner(*args,**kwargs):
        print("checking authentication")
        func(*args,**kwargs)
    return inner
def payment_required(func):
    def inner(*args,**kwargs):
        print("checking payment status")
        func(*args,**kwargs)
    return inner
@auth_required
@payment_required
def download_course():
    print("downloaded course")
download_course()