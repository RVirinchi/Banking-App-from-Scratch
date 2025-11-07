# Banking Application #
This application is divided into 3 parts:  
Part A - core - this folder contains all the python files that are independent of each other. These cannot be run directly, they have to be used within the main function in main.py.

1. account.py - This file contains the account class that handles all functionalities related to a bank account like deposit, withdraw, transfer etc.  
2. auth.py - handles new user registration and login  
3. transaction.py - this handles writing the transactions to csv and displaying them.  
4. user.py - this contains user class which holds details of user.  

Part B - data - this folder contains all the csv files.

1. accounts.csv - holds the accounts data
2. transactions.csv - holds the transactions data along with their data and time
3. users.csv - contains the users data.  

Part C - main.py  
This runs everything. It imports the core python files and takes input from user and based on that decides what to do.