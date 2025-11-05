import os
import hashlib as hl
import pandas as pd

root = os.getcwd()

def user_registration(username, password):
    # check if username already exists
    if not check_username_unique(username):
        return (False, 'username exists, choose another')
    
    # hash the password
    encoded_password = password.encode('utf-8')
    hashed_password = hl.sha256(encoded_password).hexdigest()

    # create dataframe
    df = pd.DataFrame({'username': [username], 'password': [hashed_password]})
    
    if not os.path.exists(os.path.join(root, 'csv', 'users.csv')):
        df.to_csv(os.path.join(root, 'csv', 'users.csv'), index = False)
    else:
        df.to_csv(os.path.join(root, 'csv', 'users.csv'), mode = 'a', index = False, header = False)
    
    return (True, 'user registration successful')

def check_username_unique(username):
    return True