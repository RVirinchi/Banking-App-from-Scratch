# this is the entry point of the application

from core.user import user
from core.auth import auth
from core.account import account
import pandas as pd

USERS = 'data/users.csv'


def main():
    # this flag controlls when the program exits
    flag = True

    # create the required objects
    auth_obj = auth()

    while(flag):   
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
                if len(mobile_no) > 10 or not mobile_no.isnumeric():
                    print("Invalid mobile number, try again!")
                elif auth_obj.register(username, password, name, mobile_no):
                    print("Registration successful, congratulations")
                    break
                else:
                    print("Username already exists, try with different username or login")

            # existing user login
            case '2':
                username = input("Enter ur username: ")
                password = input("Enter a strong password: ")
                if auth_obj.login(username, password):
                    print(f"Login successful, what do u wish to do today {username}")
                    post_login(account.load_account(username))
                else:
                    print("Invalid credentials, try again")

            case '3':
                flag = False

            case default:
                print("Invalid choice, choose again")

# post login function
def post_login(acc_obj: account):
    # flag to control when to exit
    flag = True
    while(flag):
        print("what do u wish to do today?")
        print("1. Deposit 2. Withdraw 3. Transfer 4. Exit")
        choice = input("Enter ur choice: ")
        match choice:
            case '1':
                amount = input("How much do u wish to deposit?: ")
                if acc_obj.deposit(amount):
                    print("Deposit successful")
                else:
                    print("deposit failed, try again.")
            
            case '2':
                amount = input("How much do u wish to withdraw?: ")
                if acc_obj.withdraw(amount):
                    print("Witchdraw successful")
                else:
                    print("withdraw failed, try again.")

            case '3':
                to_username = input("Who do u wish to send money to?")
                df = pd.read_csv(USERS)
                if df[df['username'] == to_username].empty:
                    print("The username provided doesnt exist in our bank")
                else:
                    amount = input("How much do u want to transfer?: ")
                    if acc_obj.transfer(to_username, amount):
                        print("Transaction successful")
                    else:
                        print("Invalid amount, try again")

            case '4':
                flag = False

if __name__ == "__main__":
    main()
