# this is the account class

import pandas as pd

class account:
    # instance variables
    def __init__(self, username, account_number, balance = 0.00, acc_type = "SAVINGS"):
        self.username = username
        self.account_number = account_number
        self.balance = balance
        self.acc_type = acc_type

    # instance methods
    def deposit(self, amount):
        if amount <= 0:
            return False
        self.balance += amount
        return True
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True
    
    def to_dict(self):
        return {
            'username': self.username,
            'account_number': self.account_number,
            'balance': self.balance,
            'acc_type': self.acc_type
        }
