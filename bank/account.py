class Account(object):
  def __init__(self, account_number, balance):
    self.account_number = account_number
    self.balance = balance

class Withdraws(object):
  def __init__( self, acount_number,balance,withdraw):
    self.balance = balance-withdraw

class Check_balance(object):  
  def __init__(self, balance):
    if type(balance) == int:
      return balance
    else:
      raise TypeError("Invalid type: {}".format(type(balance)))      
