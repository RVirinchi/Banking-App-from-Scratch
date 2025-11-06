# this holds the transaction class

import datetime as dt

class transaction:
    # instance variable
    def __init__(self, from_username, to_username, amount):
        self.from_username = from_username
        self.to_username = to_username
        self.amount = amount
        self.datetime = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'from_username': self.from_username,
            'to_username': self.to_username,
            'amount': self.amount,
            'date_time': self.datetime
        }