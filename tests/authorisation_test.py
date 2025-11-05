import os
import sys

# add main directory path so that we can use import call
bank = os.getcwd()
sys.path.append(bank)

from features import authorisation

def test_user_registration(username, password):
    if authorisation.user_registration(username, password):
        print("new user registration test passed")
    else:
        print("new user registration test failed")

if __name__ == '__main__':
    # enter username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # call test
    test_user_registration(username, password)
