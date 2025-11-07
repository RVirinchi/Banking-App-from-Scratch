# this is the account class

import pandas as pd
from core.transaction import transaction

class account:
    # file path
    ACC_FILE = 'data/accounts.csv'

    def __init__(self, username, account_number, balance = 0.00, acc_type = "SAVINGS"):
        # instance variables
        self.username = username
        self.account_number = account_number
        self.balance = balance
        self.acc_type = acc_type

    # instance methods
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        trnsxn_obj = transaction(self.username, self.username, amount)
        trnsxn_obj.record_transaction()
        self.save_account()
        return True
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        trnsxn_obj = transaction(self.username, self.username, amount * -1) # withdraw is negetive
        trnsxn_obj.record_transaction()
        self.save_account()
        return True
    
    def transfer(self, to_username, amount) -> bool:
        if amount < 0 or amount < self.balance:
            return False
        self.balance -= amount
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
        acc_data = df[df['username'] == username]   
        return account(acc_data['username'], acc_data['acc_number'], acc_data['balance'], acc_data['acc_type'])
    
    def to_dict(self) -> dict:
        return {
            'username': self.username,
            'account_number': self.account_number,
            'balance': self.balance,
            'acc_type': self.acc_type
        }
