class Account(object):
    """Initialize"""
    def __init__(self, account_number, balance): #pragma: no cover
      self.account_number = account_number
      self.balance = balance

class Withdraws(object):
    """For withdraws"""
    def __init__(self, balance, withdraw): #pragma: no cover
      self.balance = balance - withdraw
