from Account import account
print("Welcome to your bank!")
print("1. Create an Account")
sel = input("Please select on option by inserting a number: ")

if sel == "1":
    account.create_account()
