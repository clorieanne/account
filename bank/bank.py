"""Bank module"""
class Bank(object):
    """Bank class"""
    def __init__(self):
        """Initialization"""
        self.accounts = {}

    def add_account(self, account):
        """adding account"""
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_number):
        """getting the balance"""
        return self.accounts.get(account_number)

    def account_exist(self, account_number):
        """check if account exist"""
        return self.accounts.get(account_number) != 'None'
