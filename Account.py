import json
import random

class account:
    def __init__(self, account_number, account_type, customer_id, balance = 0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.customer_id = customer_id
        self.balance = balance
    
    
    def login():
        try:
            data = "accounts.json"
            account_number = int(input("Enter your account number (Ensure no letters are inserted): "))
            password = input("Enter your password: ")
        
            with open(data, "r") as file:
                accounts = json.load(file)

            for i in range(len(accounts)):
                if "customer" in accounts[i]:
                    for customer_data in accounts[i]["customer"]:
                        for acc in customer_data["accounts"]:
                            if acc["account_number"] == account_number and acc["password"] == password:
                                customer = Customer(
                                    customer_id=customer_data["customer_id"],
                                    fname=customer_data["first_name"],
                                    lname=customer_data["last_name"],
                                    address=customer_data["address"],
                                    contact_info=customer_data["contact_info"],
                                    password=customer_data["password"],
                                )
                                customer.accounts = customer_data["accounts"]
                                Customer.accounts_dashboard(customer)
                                return
        except FileNotFoundError:
            print("Couldn't find file")
        except Exception as e:
            print(f"An error occurred: {e}")
                
    

    def deposit():
        try:
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
        except ValueError:
            print("Invalid syntax, please tray again")
        except FileNotFoundError:
            print("Couldn't find file")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        
    def withdraw():
        try:
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
        except ValueError:
            print("Invalid syntax, please tray again")
        except FileNotFoundError:
            print("Couldn't find file")
        except Exception as e:
            print(f"An error occurred: {e}")
        


    def transfer():
        try:
            sender = int(input("Enter the account you want to send from: "))
            payee = int(input("Enter the payee account: "))
            amount = float(input("Enter the amount to transfer: "))

            sender_acc = None
            payee_acc = None

            with open("accounts.json", "r+") as file:
                data = json.load(file)

                
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
                
                elif sender_acc["account_type"] != payee_acc["account_type"]:
                    print("Unable to transfer to different account types")
                    return
                
                elif sender_acc["balance"] < amount:
                    print("Sender has insufficient balance.")
                    return

                
                sender_acc["balance"] -= amount
                payee_acc["balance"] += amount
                print(f"Success! New balance for sender: £{sender_acc['balance']}")

                
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
        except ValueError:
            print("Invalid syntax, please tray again")
        except FileNotFoundError:
            print("Couldn't find file")
        except Exception as e:
            print(f"An error occurred: {e}")
        
            


    
from Customer import Customer