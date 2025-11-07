# this file authenticates passwords

import pandas as pd
import os
from core.user import user
from core.account import account

class auth:
    # users csv file path
    FILE = "data/users.csv" # forward slash works on windows too after recent updates !!!!

    def __init__(self):
        # create the csv if it doesnt already exist
        if not os.path.exists(self.FILE):
            pd.DataFrame(columns=['username', 'password_hash', 'name', 'email']).to_csv(self.FILE, index = False)

    def register(self, username, password, name, email):
        df = pd.read_csv(self.FILE)
        # check if username exists
        if username in df['username'].values:
            return False
        
        # read the csv into df, append df, overwrite the csv
        new_user = user(username, password, name, email)
        df.loc[len(df)] = [new_user.username, new_user.password_hash, new_user.name, new_user.email]
        df.to_csv(self.FILE, index = False)

        # create new account for the user in accounts
        acc_obj = account(username, username.encode('utf-8'))

        # registration successful
        return True
    
    def login(self,username, password):
        df = pd.read_csv(self.FILE)
        # check if username exists
        if username not in df['username'].values:
            return False
        
        user_row = df[df['username'] == username].iloc[0]
        # if password matches, make new obj and return it
        if user._hash_password(password) == user_row['password_hash']:
            return user(username, password, user_row['name'], user_row['email'])
        else:
            return False