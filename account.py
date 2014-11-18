class Bank(object):
  
  
  def __init__(self):
    self.accounts = {}


  def add_account(self, account):
    self.accounts[account.account_number] = account.balance
  
  
  def get_account_balance(self, account_number):
    return self.accounts.get(account_number)
  
  
  def withdraw_account(self, account, amount):
    balance = self.accounts[account.account_number] = account.balance - amount
    return balance
  

  def account_exist(self, account)
    return self.accounts[account] == account

  
          
