import json
import random

class account:
    def __init__(self, account_number, account_type, customer_id, balance):
        self.account_number = account_number
        self.account_type = account_type
        self.customer_id = customer_id
        self.balance = balance
    
    
    def login():
        data = "accounts.json"
        account_number = int(input("Enter your account number (Ensure no letters are inserted): "))
        password = input("Enter your password: ")


    
        with open(data, "r") as file:
            accounts = json.load(file)

        for i in range(len(accounts)):
            if "customer" in accounts[i]:
                for customer in accounts[i]["customer"]:
                    for acc in customer["accounts"]:
                        if acc["account_number"] == account_number and acc["password"] == password:
                            Customer.view_accounts(customer)
                            return Customer
                        else:
                            print("Invalid password or account try again")

                
    
    def deposit():
        account_number = int(input("Enter the account number for deposit: "))
        amount = float(input("Enter the amount to deposit: "))

        with open("accounts.json", "r+") as file:
            data = json.load(file)
            for i in data:
                if "customer" in i:
                    for customer in i["customer"]:                            
                        for acc in customer["accounts"]:
                            if acc["account_number"] == account_number:
                                acc["balance"] += amount
                                print(f"Deposit successful! New balance: £{acc['balance']}")
                                file.seek(0)
                                json.dump(data, file, indent=4)
                                file.truncate()
                                return
        print("Account not found.")

    def withdraw():
        account_number = int(input("Enter the account number for withdrawal: "))
        amount = float(input("Enter the amount to withdraw: "))

        with open("accounts.json", "r+") as file:
            data = json.load(file)
            for record in data:
                if "customer" in record:
                    for customer in record["customer"]:
                          for acc in customer["accounts"]:
                              if acc["account_number"] == account_number:
                                  if acc["balance"] >= amount:
                                      acc["balance"] -= amount
                                      print(f"Withdrawal successful! New balance: £{acc['balance']}")
                                      file.seek(0)
                                      json.dump(data, file, indent=4)
                                      file.truncate()
                                      return
                                  else:
                                      print("Insufficient funds.")
                                      return
        print("Account not found")


    def transfer():
        sender = int(input("Enter the account you want to send from: "))
        payee = int(input("Enter the payee account: "))
        amount = float(input("Enter the amount to transfer: "))

        with open("accounts.json", "r+") as file:
            data = json.load(file)

            # Find source and destination accounts
            for i in data:
                if "customer" in i:
                    for customer in i["customer"]:
                        for acc in customer["accounts"]:
                            if acc["account_number"] == sender:
                                sender_acc = acc
                            if acc["account_number"] == payee:
                                payee_acc = acc

            if not sender_acc or not payee_acc:
                print("Sender, Payee or both have no been found")
                return

            if sender_acc["account_type"] != payee_acc["account_type"]:
                print("Unable to transfer to different account types")
                return

            if sender_acc["balance"] < amount:
                print("Sender has insufficient balance.")
                return

            # Perform the transfer
            sender_acc["balance"] -= amount
            payee_acc["balance"] += amount
            print(f"Success! New balance for sender: £{sender_acc['balance']}")

            # Save changes to JSON
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
        

    def check_balance():
        print("4")
    
from Customer import Customer