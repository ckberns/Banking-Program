"""
Program: bank_account.py
Author: Brandon Kerns
Last Date Modified: 1/31/24
The purpose of this program is to utilize OOP practices to create a bank account application. First, a class titled
UserAccount will be defined that will contain the methods used within this program. Next, two account objects will be
instantiated that will allow the user to interact with the program. One object will be used for a checking account,
while the other will be used for a savings account. Then, the user will be asked the type of transaction they wish to
complete on their account. Finally, after all transactions have been processed, the program will display the general
information about the user's account.
"""
from UserAccount import UserAccount

# Create two objects from the UserAccount class. A checking account, and savings account.
account1 = UserAccount("Jane Smith", "Checking", 12345)
account2 = UserAccount("John Doe", "Savings", 67890)

if __name__ == "__main__":
    # Use the created objects to call the different functions within the class.
    acct_access = input("Would you like to access your Checking or Savings account? ").title()
    if acct_access == "Checking":
        # Prompt the user to make a transaction. Utilize a loop to allow the user to make multiple transactions at once.
        while True:
            acct_action = input("Would you like to 'Deposit' or 'Withdraw'? (Press 'F' when finished): ").title()
            if acct_action == "Deposit":
                account1.deposit()
            elif acct_action == "Withdraw":
                account1.withdrawal()
            elif acct_action == "F":
                break
            else:
                print("Invalid entry! Please only enter 'Deposit' or 'Withdraw'.")
        # Display the account balance after all transactions have been processed.
        account1.display()
    elif acct_access == "Savings":
        while True:
            acct_action = input("Would you like to 'Deposit' or 'Withdraw'? (Press 'F' when finished): ").title()
            if acct_action == "Deposit":
                account2.deposit()
            elif acct_action == "Withdraw":
                account2.withdrawal()
            elif acct_action == "F":
                break
            else:
                print("Invalid entry! Please only enter 'Deposit' or 'Withdraw'.")
        account2.display()
    else:
        print("Invalid entry! You must select from the choices provided. Please try again.")
