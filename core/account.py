# this is the account class

import pandas as pd
from core.transaction import transaction
from core.user import user

class account:
    # file path
    ACC_FILE = 'data/accounts.csv'
    USERS = 'data/users.csv'

    def __init__(self, username, account_number, balance = '0.0', acc_type = "SAVINGS"):
        # instance variables
        self.username = username
        self.account_number = account_number
        self.balance = balance
        self.acc_type = acc_type

    # instance methods
    def deposit(self, amount: str):
        if amount <= '0':
            return False
        self.balance = str(int(self.balance) + int(amount))
        trnsxn_obj = transaction(self.username, self.username, amount)
        trnsxn_obj.record_transaction()
        self.save_account()
        return True
    
    def withdraw(self, amount: str):
        if int(amount) > int(self.balance):
            return False
        self.balance = str(int(self.balance) - int(amount))
        trnsxn_obj = transaction(self.username, self.username, str(int(amount) * -1)) # withdraw is negetive
        trnsxn_obj.record_transaction()
        self.save_account()
        return True
    
    def transfer(self, to_username, amount) -> bool:
        if int(amount) < 0 or int(amount) > int(self.balance):
            return False
        self.balance = str(int(self.balance) - int(amount))
        # update balance of the the other account
        df = pd.read_csv(account.USERS)
        new_balance = int(df[df['username'] == to_username]['balance'].iloc[0]) + int(amount)
        df.loc[df['username'] == to_username, 'balance'] = new_balance
        
        trnsxn_obj = transaction(self.username, to_username, amount)
        trnsxn_obj.record_transaction()
        self.save_account()
        return True
    
    def save_account(self):
        df = pd.read_csv(self.ACC_FILE)
        df = df[df['username'] != self.username]
        df.loc[len(df)] = self.to_dict()
        df.to_csv(self.ACC_FILE, index=False)

    # load account details from csv and return account object
    @classmethod
    def load_account(cls, username):
        df = pd.read_csv(account.ACC_FILE)
        acc_data: pd.Series = df[df['username'] == username].iloc[0]
        return account(acc_data['username'], acc_data['acc_no'], acc_data['balance'], acc_data['acc_type'])
    
    def to_dict(self) -> dict:
        return {
            'username': str(self.username),
            'account_number': str(self.account_number),
            'balance': str(self.balance),
            'acc_type': str(self.acc_type)
        }
