from Account import account
from Customer import Customer

print("Welcome to our bank!")
print("1. Create a Log in")
print("2. Log in")
print("3. Account information retrieval")

try:
    sel = input("Please select on option by inserting a number: ")


    if sel == "1":
        customer_id = Customer.customer_id_generator()
        fname = input("Please insert your first name: ")
        lname = input("Please insert your last name: ")
        address = input("Please insert your address: ")
        contact_info = input("Please insert your contact information: ")

        while True:
            password = input("Enter a password: ")
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                break
            else:
                print("This does not match please try again")

        customer = Customer(customer_id, fname, lname, address, contact_info,password)
        customer.create_account()
        Customer.accounts_dashboard(customer)

    elif sel == "2":
        account.login()

    elif sel == "3":
        Customer.retrieve_account_info()
    else:
        print("Invalid syntax please try again")
except Exception as e:
        print(f"An error occurred when using the home page please try again: {e}")
