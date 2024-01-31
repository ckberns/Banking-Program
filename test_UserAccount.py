import unittest
from UserAccount import UserAccount


# Create the class that will test the UserAccount class.
class TestUserAccount(unittest.TestCase):
    # Define the setup method to run before each test.
    def setUp(self):
        self.account1 = UserAccount("John", "Checking", 123456)
        self.account2 = UserAccount("Jane", "Savings", 789101)

    # Define the teardown method to run after each test completes.
    def tearDown(self):
        del self.account1
        del self.account2

    # Define a test for the deposit method to ensure the method functions as anticipated.
    def test_deposit(self):
        result = self.account1.deposit()
        self.assertIsNone(result)

    # Define a test for the withdrawal method to ensure the method functions as anticipated.
    def test_withdrawal(self):
        result = self.account2.withdrawal()
        self.assertIsNone(result)

    # Define a test to ensure the display method functions as anticipated.
    def test_display(self):
        result = self.account1.display()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
