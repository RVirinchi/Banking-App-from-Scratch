import pandas as pd
from core.transaction import transaction

class account:
    # file path
    ACC_FILE = 'data/accounts.csv'

    def __init__(self, username, account_number, balance=0.0, acc_type="SAVINGS"):
        self.username = username
        self.account_number = account_number
        self.balance = float(balance)
        self.acc_type = acc_type

    def deposit(self, amount: float): # returns true if successfull else false, same for the withdraw function as well
        amount = float(amount)
        if amount <= 0:
            print("Invalid deposit amount")
            return False

        self.balance += amount
        trnsxn_obj = transaction(self.username, self.username, amount)
        trnsxn_obj.record_transaction()
        # save to csv
        self.save_account()
        return True

    def withdraw(self, amount: float):
        amount = float(amount)
        if amount <= 0 or amount > self.balance:
            print("Insufficient balance or invalid amount")
            return False

        self.balance -= amount
        trnsxn_obj = transaction(self.username, self.username, -amount)  # negative transaction
        trnsxn_obj.record_transaction()
        # save to csv
        self.save_account()
        return True

    def transfer(self, to_username: str, amount: float) -> bool:
        amount = float(amount)
        if amount <= 0 or amount > self.balance:
            print("Invalid or insufficient funds for transfer")
            return False
        self.balance -= amount
        # Load account from CSV
        df = pd.read_csv(self.ACC_FILE)
        # Check to_username exists
        if to_username not in df['username'].values:
            return False

        # Update to_users balance
        receiver_balance = float(df.loc[df['username'] == to_username, 'balance'].iloc[0])
        new_balance = receiver_balance + amount
        df.loc[df['username'] == to_username, 'balance'] = new_balance

        # Update from_users ablance
        df.loc[df['username'] == self.username, 'balance'] = self.balance
        df.to_csv(self.ACC_FILE, index=False)
        # write the transaction to csv
        trnsxn_obj = transaction(self.username, to_username, amount)
        trnsxn_obj.record_transaction()
        return True
    
    def save_account(self):
        df = pd.read_csv(self.ACC_FILE)

        # check if user already exists
        if self.username in df['username'].values:
            df.loc[df['username'] == self.username, ['acc_no', 'balance', 'acc_type']] = [
                self.account_number, self.balance, self.acc_type
            ]
        else:
            # add as new record
            df.loc[len(df)] = self.to_dict()

        # save to CSV
        df.to_csv(self.ACC_FILE, index=False)

    @classmethod
    def load_account(cls, username):
        df = pd.read_csv(cls.ACC_FILE)
        if username not in df['username'].values:
            return None
        acc_data = df.loc[df['username'] == username].iloc[0]
        return cls(acc_data['username'],acc_data['acc_no'],acc_data['balance'],acc_data['acc_type'])

    def to_dict(self) -> dict:
        return {
            'username': self.username,
            'acc_no': self.account_number,
            'balance': self.balance,
            'acc_type': self.acc_type
        }
