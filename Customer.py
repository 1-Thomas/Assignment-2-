import tkinter as tk
from tkinter import messagebox
from SaveToJson import SaveToJson
import random
import json


class Customer:
    def __init__(self, customer_id, fname, lname, address, contact_info, password):
        self.customer_id = customer_id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.contact_info = contact_info
        self.password = password
        self.accounts = []

    def create_account(self):
        try:
            print(f"Welcome to the bank!")
            print("1. Savings")
            print("2. Current")
            print("3. Mortgage")
            while True:
                account_type_choice = input("Please insert a number to select an account type: ")
                if account_type_choice == "1":
                    account_type = "Savings"
                    break
                elif account_type_choice == "2":
                    account_type = "Current"
                    break
                elif account_type_choice == "3":
                    account_type = "Mortgage"
                    break
                else:
                    print("Invalid Syntax")

            balance = float(input("How much would you like to deposit into the account: "))
            account_number = random.randint(100000, 200000)


            new_account = {
                "account_number": account_number,
                "account_type": account_type,
                "customer_id": self.customer_id,
                "password": self.password,
                "balance": balance,
            }
        
            self.accounts.append(new_account)
        
            
            customer_data = {
                "customer": [{
                    "customer_id": self.customer_id,
                    "first_name": self.fname,
                    "last_name": self.lname,
                    "address": self.address,
                    "contact_info": self.contact_info,
                    "password": self.password,
                    "accounts": self.accounts
                }]
            }
            SaveToJson.save_to_json("accounts.json", customer_data)
            print(f"Welcome to our bank here is your account number {account_number}")
        except Exception as e:
            print(f"An error occurred when trying to create an account please try again: {e}")

    def accounts_dashboard(self):
        while True:
            try:
                print("1. View Accounts")
                print("2. Open a New Account")
                print("3. Deposit")
                print("4. Withdraw")
                print("5. Transfer")           
                print("6. Logout")
                sel = input("Enter your choice: ")
                if sel == "1":
                    for acc in self.accounts:
                        print(f"Account Number: {acc['account_number']}, "
                            f"Account Type: {acc['account_type']}, "
                            f"Balance: £{acc['balance']}")
                elif sel == "2":
                    Customer.create_account(self)
                elif sel == "3":
                    account.deposit()
                elif sel == "4":
                    account.withdraw()
                elif sel == "5":
                    account.transfer()
                elif sel == "6":
                    print("Logging out...")
                    break
                else:
                    print("Please try again, invalid input.")
            except Exception as e:
                print(f"An error occured when accessing the accounts dashboard please try again: {e}")

    

    def customer_id_generator():
        try:
            file_name = "accounts.json"
            with open(file_name, "r") as file:
                accounts = json.load(file)
                next_id = 1
                for i in range(len(accounts)):
                    if "customer" in accounts[i]:
                        for customer in accounts[i]["customer"]:
                            for acc in customer["accounts"]:
                                next_id = max(next_id, acc["customer_id"] + 1)
                return next_id 
        except FileNotFoundError:
            print("Couldn't find file.")
            return 1
        except json.JSONDecodeError:
            print("Error reading JSON file.")
            return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return 1

        
    def retrieve_account_info():
        try:
            account_number = int(input("Enter the account number: "))
            file_name = "accounts.json"
            
            with open(file_name, "r") as file:
                accounts_data = json.load(file)
                for record in accounts_data:
                    if "customer" in record:
                        for customer in record["customer"]:
                            for acc in customer["accounts"]:
                                if acc["account_number"] == account_number:
                                    print(f"Account Information:\nCustomer Name: {customer['first_name']} {customer['last_name']}\nAccount Type: {acc['account_type']}")
                                    return
        except ValueError:
            print("Invalid syntax, please try again.")
        except FileNotFoundError:
            print("Couldn,t find file")
        except Exception as e:
            print(f"An error occurred: {e}")
from Account import account