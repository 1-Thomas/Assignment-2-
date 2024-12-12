class Customer:
    def __init__(self, customer_id, name, address, contact_info):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.accounts = []

    def create_account(self, bank, account_type):
        print("1")

    def view_accounts(self):
        print("2")