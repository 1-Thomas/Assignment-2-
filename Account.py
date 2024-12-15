import json
import random
class account:
    def __init__(self, account_number, account_type, customer_id, balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.customer_id = customer_id
        self.balance = balance
    
    

    
    
    def create_account():
        data = "accounts.json"
        fname = input("Please insert your first name: ")
        lname = input("Please insert your last name: ")
        address = input("Please insert your address: ")
        contact_info = input("Please insert your contact information: ")
        account_type = input("What are you using the account for savings, current or mortgage?): ")
        
        automatic_account_number = random.randint(100000, 200000)
        
        while True:
            password = input("Enter a password: ")
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                break
            else:
                print("This does not match please try again")

        
    

        balance = float(input("How much would you like to deposit into th account?"))
        account_number = automatic_account_number

        account = {
            "account_number": account_number,
            "first name": fname,
            "last name": lname,
            "address": address,
            "contact_info": contact_info,
            "account_type": account_type,
            "password": password,
            "balance": balance
        }


        with open(data, "r") as file:
            accounts = json.load(file)
    

        accounts.append(account)

        # Write the updated list back to the JSON file
        with open(data, "w") as file:
            json.dump(accounts, file, indent=4)

        print(f"Welcome to our bank, here is your account number {account_number}")

    
    def deposit():
        print("1")

    def withdraw():
        print("2")

    def transfer():
        print("3")

    def check_balance():
        print("4")
    
