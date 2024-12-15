from Account import account
class Customer:
    def __init__(self, customer_id, name, address, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.accounts = []

    def create_account(self):
        account.create_account(self)

    def view_accounts():
        print("2")