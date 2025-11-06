# this file manages everything
import pandas as pd
import os
from core.account import account
from core.transaction import transaction

class controller:

    def __init__(self):
        # instance variable
        self.ACC_FILE = 'data/accounts.csv'
        self.TRNSXN_FILE = 'data/transactions.csv'
        self.USER_FILE = 'data/user.csv'

        # check if the files exist or not
        if os.path.exists(self.ACC_FILE):
            pd.DataFrame(columns = ['username', 'acc_number', 'balance', 'acc_type']).to_csv(self.ACC_FILE, index = False)
        if os.path.exists(self.TRNSXN_FILE):
            pd.DataFrame(columns = ['from_username', 'to_username', 'amount']).to_csv(self.TRNSXN_FILE, index = False)
        
    # load account details from csv
    def load_account(self, username):
        df1 = pd.read_csv(self.ACC_FILE)
        df2 = pd.read_csv(self.USER_FILE)
        user_row = df1[df1['username'] == username]

        # if no account exists with that username but it is a valid user then create a new account
        if df2[df2['username'] == username]:
            # username is legit
            if user_row.empty:
                acc_number = len(df1) + 1001
                acc = account(username, acc_number)
                self.save_account(acc)
                return acc
            else:
                # account exists so return new obj with the values in csv
                return account(user_row['username'], user_row['account_number'], user_row['balance'], user_row['acc_type'])
        else:
            return None
    
    def save_account(self, account):
        df = pd.read_csv(self.ACC_FILE)
        df = df[df['username'] != account.username]
        df.loc[len(df)] = account.to_dict()
        df.to_csv(self.ACC_FILE, index=False)

    def record_transaction(self, transaction):
        df = pd.read_csv(self.TRNSXN_FILE)
        df.loc[len(df)] = transaction.to_dict()
        df.to_csv(self.TRNSXN_FILE, index = False)

    def get_transaction_history(self, username):
        df = pd.read_csv(self.TRNSXN_FILE)
        return df[df['username'] == username]