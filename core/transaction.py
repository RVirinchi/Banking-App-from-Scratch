# this holds the transaction class

import datetime as dt
import pandas as pd

class transaction:
    # file path
    TRNSXN_FILE = 'data/transactions.csv'

    # instance variable
    def __init__(self, from_username, to_username, amount):
        self.from_username = from_username
        self.to_username = to_username
        self.amount = amount
        self.datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def record_transaction(self):
        df = pd.read_csv(self.TRNSXN_FILE)
        df.loc[len(df)] = self.to_dict()
        df.to_csv(self.TRNSXN_FILE, index = False)

    @classmethod
    def display_transactions(cls, from_username):
        df = pd.read_csv(transaction.TRNSXN_FILE)
        transactions = df[df['from_username'] == from_username]
        print("====== TRANSACTIONS ======")
        print(transactions)

    def to_dict(self) -> dict:
        return {
            'from_username': self.from_username,
            'to_username': self.to_username,
            'amount': self.amount,
            'date_time': self.datetime
        }