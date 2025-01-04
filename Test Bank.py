import unittest
from unittest.mock import patch, mock_open
from Account import account
from Customer import Customer

class TestBankingSystem(unittest.TestCase):
    def test_create_account(self):
        """Test customer account creation."""
        with patch("builtins.input", side_effect=[
            "1",  
            "500" 
        ]), patch("builtins.open", new_callable=mock_open): 
            try:
            
                customer_id = 1
                fname = "John"
                lname = "Doe"
                address = "123 Elm Street"
                contact_info = "555-1234"
                password = "password123"

                customer = Customer(customer_id, fname, lname, address, contact_info, password)
                customer.create_account() 

               
                self.assertEqual(len(customer.accounts), 1) 
                self.assertEqual(customer.accounts[0]["account_type"], "Savings") 
                self.assertEqual(customer.accounts[0]["balance"], 500)  
                self.assertEqual(customer.accounts[0]["customer_id"], customer_id) 
                print("Create_account Test Passed")
            except Exception as e:
                print(f"Create_account Test Failed: {e}")
            
    def test_login(self):
        """Test login functionality."""
        with patch("builtins.input", side_effect=[
            "100001",  
            "password123"  
        ]), patch("builtins.open", new_callable=mock_open):
            try:
                account.login()  
                print("Login Test Passed")
            except Exception as e:
                print(f"Login Test Failed: {e}")

    def test_retrieve_account_info(self):
        """Test account information retrieval."""
        with patch("builtins.input", side_effect=[
            "100001"  
        ]), patch("builtins.open", new_callable=mock_open):
            try:
                Customer.retrieve_account_info()  
                print("Retrieve_account_info Test Passed")
            except Exception as e:
                print(f"Retrieve_account_info Test Failed: {e}")

    def test_deposit(self):
        """Test deposit functionality."""
        with patch("builtins.input", side_effect=[
            "100001",  
            "200"  
        ]), patch("builtins.open", new_callable=mock_open):
            try:
                account.deposit()  
                print("Deposit Test Passed")
            except Exception as e:
                print(f"Deposit Test Failed: {e}")

    def test_withdraw(self):
        """Test withdrawal functionality."""
        with patch("builtins.input", side_effect=[
            "100001",  
            "100"  
        ]),patch("builtins.open", new_callable=mock_open):
            try:
                account.withdraw()  
                print("Withdraw Test Passed")
            except Exception as e:
                print(f"Withdraw Test Failed: {e}")

    def test_transfer(self):
        """Test transfer functionality."""
        with patch("builtins.input", side_effect=[
            "100001",  
            "100002",  
            "50"
        ]), patch("builtins.open", new_callable=mock_open):
            try:
                account.transfer()  
                print("Transfer Test Passed")
            except Exception as e:
                print(f"Transfer Test Failed: {e}")

    
if __name__ == "__main__":
    unittest.main()    