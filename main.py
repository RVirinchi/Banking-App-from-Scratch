# this is the entry point of the application

from core.user import user
from core.auth import auth
from core.account import account
import pandas as pd
import os

USERS = 'data/users.csv'
ACCOUNTS = 'data/accounts.csv'
TRANSACTIONS = 'data/transactions.csv'

# global flags, used to exit infinite loops
flag_main = True
flag_login =True


def main():

    # init all files (if they dont exsit)
    if not os.path.exists(USERS):
        pd.DataFrame(columns = ['username', 'password_hash', 'name', 'mobile_no']).to_csv(USERS, index = False) # type: ignore (supress warning of type error)
    if not os.path.exists(ACCOUNTS):
        pd.DataFrame(columns = ['username', 'acc_no', 'balance', 'acc_type']).to_csv(ACCOUNTS, index = False) # type: ignore (supress warning of type error)
    if not os.path.exists(TRANSACTIONS):
        pd.DataFrame(columns = ['from_username', 'to_username', 'amount', 'datetime']).to_csv(TRANSACTIONS, index = False) # type: ignore (supress warning of type error)

    # create the required objects
    auth_obj = auth()
    print("") # just to add readability in terminal
    print("=============== WELCOME TO TRUSTUS BANK ===============")
    print("choose: 1. Register 2. Login 3. Exit")
    choice = input("choice: ")

    # do something based on the input given
    match choice:
        # new registration
        case '1':
            username = input("Enter ur username: ")
            password = input("Enter a strong password: ")
            name = input("Enter ur name: ")
            mobile_no = input("Enter 10 digit mobile number: ")
            if len(mobile_no) != 10 or not mobile_no.isnumeric():
                print("Invalid mobile number, try again!")
            elif auth_obj.register(username, password, name, mobile_no):
                print("Registration successful, congratulations")
            else:
                print("Username already exists, try with different username or login")

        # existing user login
        case '2':
            username = input("Enter ur username: ")
            password = input("Enter ur password: ")
            if auth_obj.login(username, password):
                print(f"Login successful, what do u wish to do today {username}")
                global flag_login
                flag_login = True
                while(flag_login):
                    acc_obj = account.load_account(username)
                    if acc_obj is not None:
                        post_login(acc_obj)
                    else:
                        flag_login = False
                        print("Something went wrong")
            else:
                print("Invalid credentials, try again")

        case '3':
            global flag_main
            flag_main = False

        case default:
            print("Invalid choice, choose again")

# post login function
def post_login(acc_obj: account):
    print("\nwhat do u wish to do today?")
    print("1. Deposit 2. Withdraw 3. Transfer 4. View details 5. Exit")
    choice = input("Enter ur choice: ")
    match choice:
        case '1':
            amount = int(input("How much do u wish to deposit?: "))
            if acc_obj.deposit(amount):
                print("Deposit successful")
            else:
                print("deposit failed, try again.")
        
        case '2':
            amount = int(input("How much do u wish to withdraw?: "))
            if acc_obj.withdraw(amount):
                print("Witchdraw successful")
            else:
                print("withdraw failed, try again.")

        case '3':
            to_username = input("Who do u wish to send money to? ")
            df = pd.read_csv(USERS)
            if df[df['username'] == to_username].empty:
                print("The username provided doesnt exist in our bank")
            else:
                amount = int(input("How much do u want to transfer?: "))
                if acc_obj.transfer(to_username, amount):
                    print("Transaction successful")
                else:
                    print("Invalid amount, try again")

        case '4':
            print("========= YOUR ACC DETAILS ARE =========")
            df = pd.read_csv(ACCOUNTS)
            df = df[df['username'] == acc_obj.username]
            print(df)
            print("======== YOUR TRANSACTION DETAILS ARE =========")
            df = pd.read_csv(TRANSACTIONS)
            df = df[df['from_username'] == acc_obj.username]
            print(df)

        
        case '5':
            global flag_login
            flag_login = False

        case _:
            print("Invalid option, try again")


if __name__ == "__main__":
    # this flag controlls when the program exits
    while(flag_main):
        main()
