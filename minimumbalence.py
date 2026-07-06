def minimumbalence(func):
    def wrapper(balence,amount):
        if balence - amount > 1000:
            func(balence,amount)
        else:
            print("withdrawal failed minimum balence is 1000")
    return wrapper
@minimumbalence
def account(balence,amount):
    balence=balence - amount
    print("withdrawal successful")
    print("remaining balence=",balence)
balence=int(input("enter the account balence:"))
amount=int(input("enter the withdrawal amount:"))
account(balence,amount)