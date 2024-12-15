from Account import account
from Customer import Customer
print("Welcome to your bank!")
print("1. Create an Account")
print("2. Log in")
sel = input("Please select on option by inserting a number: ")


if sel == "1":
    account.create_account()

elif sel == "2":
    account.login()