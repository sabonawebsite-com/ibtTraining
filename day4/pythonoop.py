class Accounts:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_id, account_data):
        self.accounts[account_id] = account_data

    def get_account(self, account_id):
        return self.accounts.get(account_id)

    def remove_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]