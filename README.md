#Bank Management System

This project is a Bank Management System built using Tkinter for the graphical user interface (GUI) and MySQL for database management. It allows users to create accounts, log in, deposit money, withdraw money, and manage their bank account details in a simple and user-friendly interface.

##Features

    New User Registration: Allows users to create a new bank account by providing details like name, age, gender, PIN, and state.
    Login for Existing Users: Existing users can log in using their name and PIN to access their accounts.
    Deposit Money: Users can deposit money into their accounts.
    Withdraw Money: Users can withdraw money from their accounts, with balance checks in place.
    Account Deletion: Users can delete their accounts, with a confirmation prompt for security.
    Balance Check: Displays the current balance of the logged-in user.
    Interactive GUI: A simple and intuitive graphical interface built with Tkinter.

##Technologies Used

    Python: The main programming language for implementing the logic and functionality of the system.
    Tkinter: The Python library used for building the graphical user interface (GUI).
    MySQL: A relational database system used for storing user data (account details, balances, etc.).
    pymysql: A Python MySQL library used to connect and interact with the MySQL database.

##Setup Instructions
###Prerequisites

    Python 3.x: Ensure Python is installed on your machine.
    MySQL: Install MySQL or MariaDB, and set up a MySQL server.
    pymysql: Install the pymysql library to allow Python to connect with MySQL.

###Steps to Set Up

    Install Python:
        Download and install Python from the official website: https://www.python.org/downloads/
        Make sure to add Python to the system PATH during installation.

    Install MySQL:
        Install MySQL by following the instructions on the official MySQL website: https://dev.mysql.com/downloads/installer/
        Set up a MySQL server and note down the username and password.

    Install pymysql:
        Open the terminal/command prompt and install pymysql by running:

    pip install pymysql

1. Create the Database:

    Open MySQL and create the database by running the following commands:

    CREATE DATABASE bank_management;
    USE bank_management;

2. Create the Table:

    Create the New_User table using the following SQL schema:

    CREATE TABLE New_User (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        pin INT,
        state VARCHAR(100),
        gender VARCHAR(10),
        balance INT DEFAULT 0,
        account_no BIGINT
    );

3. Update Database Connection:

    Ensure the database connection in the code points to your MySQL server (localhost, username root, password password, and database bank_management).

4. Run the Application:

    After setting up the database, save the Python script, and run it:

        python bank_management_system.py

##Database Schema

The database schema used in the Bank Management System consists of the following table:
New_User Table
Column	Type	Description
id	INT AUTO_INCREMENT	Unique identifier for each user
name	VARCHAR(100)	User's full name
age	INT	User's age
pin	INT	Personal Identification Number for security
state	VARCHAR(100)	User's state of residence
gender	VARCHAR(10)	User's gender
balance	INT DEFAULT 0	User's account balance
account_no	BIGINT	Unique account number assigned to each user
## How to Use

    1. Start the Application:
        Run the script bank_management_system.py.
        The main menu will appear with options to create a new user or log in as an existing user.

    2. New User:
        Click the "New User" button to register a new user.
        Provide the required information (name, age, pin, state, and gender) to create the account.

    3. Login:
        Click the "Login User" button to log in to an existing account.
        Enter your name and PIN to access your account.

    4. Transactions:
        Once logged in, you can access the transaction menu to:
            Deposit Money: Enter the amount to deposit into your account.
            Withdraw Money: Enter the amount to withdraw, ensuring you have sufficient balance.
            Delete Account: Delete your account with a confirmation prompt.

    5. Exit:
        Click the "Exit" button to close the application.

##Contributing

Contributions are welcome! To contribute to the project, follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-name).
    Make your changes.
    Commit your changes (git commit -am 'Added new feature').
    Push to the branch (git push origin feature-name).
    Create a pull request.

##Conclusion

This Bank Management System provides a simple and efficient way to manage banking operations using a graphical interface. With features like user registration, login, balance management, and account deletion, it offers a comprehensive solution for basic banking needs. By following the setup instructions, you can easily deploy and use this system for personal or educational purposes.

#Download My Application



----

Happy Coding 


-----
