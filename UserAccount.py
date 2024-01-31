"""
This file contains the class, UserAccount, that will be used to create objects for a bank account application.
"""


# Define the UserAccount class with attributes for the account owner's name, account number, and overall balance.
class UserAccount:
    def __init__(self, account_holder, account_type, account_num):
        self.account_holder = account_holder
        self.account_type = account_type
        self.account_num = account_num
        self.account_balance = 0

    # Create a function to allow the user to deposit an amount into their account, updating the balance.
    def deposit(self):
        while True:
            try:
                total_deposit = float(input("Please enter the amount you would like to deposit: "))
                if total_deposit < 0:
                    print("You must enter an amount greater than $0.00. Please try again.")
                else:
                    self.account_balance += total_deposit
                    print(f"You deposited ${total_deposit:.2f} into your {self.account_type} account.")
                    break
            except ValueError:
                print("Invalid input! You must enter a numeric value.")

    # Create a function to allow the user withdrawal from account. Display error if the account balance is insufficient.
    def withdrawal(self):
        try:
            withdrawal_amt = float(input("Please enter the amount you would like to withdraw: "))
            if self.account_balance < withdrawal_amt:
                print("Unable to process this transaction. Your account has an insufficient balance.")
            else:
                self.account_balance -= withdrawal_amt
                print(f"You withdrew ${withdrawal_amt:.2f} from your {self.account_type} account.")
        except ValueError:
            print("Invalid input! You must enter a numeric value.")

    # Define a function that will display the account information to the user.
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Number: {self.account_num}")
        print(f"Account Balance: ${self.account_balance:.2f}")
