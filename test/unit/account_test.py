import unittest
from bank.account import *

class TestAccount(unittest.TestCase):
  def test_account_object_can_be_created(self):
    account = Account()

class TestAccount(unittest.TestCase):
  def test_account_object_returns_current_balance(self):
    account = Account("001", 50)
    self.assertEqual(account.account_number, "001")
    self.assertEqual(account.balance, 50)
 
  def test_withdraw(self):
    account = Withdraws("001", 50, 20)
    self.assertEqual(account.balance, 30)
    

if __name__ == '__main__':
  unittest.main()
