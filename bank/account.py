"""Account and Withdraw Classes"""
class Account(object):
    """Initialize"""
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

class Withdraws(object):
    """For withdraws"""
    def __init__(self, balance, withdraw):
        self.balance = balance - withdraw
