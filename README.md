# Bank Management System

This project is a *Bank Management System* implemented in Python using *Tkinter* for the user interface and *MySQL* as the database. It allows users to perform essential banking operations such as creating accounts, logging in, checking balances, depositing money, and withdrawing money.

---

## Features

- *User Creation*: New users can create accounts with a name, age, PIN, state, and gender. The system assigns a unique account number.
- *User Login*: Existing users can log in securely using their name and PIN.
- *Deposit Money*: Users can deposit money into their accounts.
- *Withdraw Money*: Users can withdraw money, ensuring there is sufficient balance.
- *Balance Display*: The current account balance is displayed during transactions.
- *Graphical Interface*: A clean, user-friendly GUI built with Tkinter.

---

## Technologies Used

- *Python*: Programming language.
- *Tkinter*: GUI library for Python.
- *MySQL*: Database for storing user data.
- *Pymysql*: Python library to connect MySQL with Python.

---

## Setup Instructions

Follow these steps to run the project on your local system:

1. *Install Required Libraries*:
   Ensure Python is installed, then run:
   bash
   pip install pymysql
   

2. *Set Up MySQL Database*:
   - Open MySQL and create a database named user.
   - Create the required table using the following SQL script:
     sql
     CREATE TABLE table1 (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(100),
         age INT,
         pin INT,
         state VARCHAR(100),
         gender VARCHAR(10),
         balance INT DEFAULT 0,
         account_no BIGINT UNIQUE
     );
     

3. *Update Database Credentials*:
   Replace the database connection details in the Python code:
   python
   connection = pymysql.connect(
       host="localhost",
       user="root",
       password="your_password",  # Replace with your MySQL password
       database="user"
   )
   

4. *Run the Application*:
   - Save the Python script to a file, e.g., bank_system.py.
   - Execute the file:
     bash
     python bank_system.py
     

---

## Database Schema

The project uses a single table table1 with the following columns:

| Column Name  | Data Type    | Description                      |
|--------------|--------------|----------------------------------|
| id         | INT          | Primary Key, Auto-incremented   |
| name       | VARCHAR(100) | User's full name                |
| age        | INT          | User's age                      |
| pin        | INT          | User's secure PIN               |
| state      | VARCHAR(100) | User's state of residence       |
| gender     | VARCHAR(10)  | User's gender                   |
| balance    | INT          | Current balance (default: 0)    |
| account_no | BIGINT       | Unique account number           |

---

## How to Use

1. *Main Menu*:
   - Click *"New User"* to create a new account.
   - Click *"Login User"* to log in with your credentials.
   - Click *"Exit"* to close the application.
  
     ![Screenshot 2024-12-17 114145](https://github.com/user-attachments/assets/279ae46d-b492-4aff-867f-da34b808df1a)


2. *Creating a User*:
   - Fill in all required fields (Name, Age, PIN, State, Gender).
   - After successful account creation, note your *Account Number*.
  
    ![Screenshot 2024-12-17 114240](https://github.com/user-attachments/assets/f9b6bb29-d50f-4dd5-8629-90ea46d2c00d)


3. *Logging In*:
   - Enter your *Name* and *PIN* to log in.
  
     ![Screenshot 2024-12-17 114307](https://github.com/user-attachments/assets/aaad8bbc-943f-4fd5-bb0b-edceb4e87550)

4. *Transactions*:
   - After logging in, view your *Current Balance*.
   - Use *Deposit* to add money to your account.
   - Use *Withdraw* to take money from your account (ensure sufficient balance).
  
     ![Screenshot 2024-12-17 114323](https://github.com/user-attachments/assets/d00194b0-6086-43ae-b45c-bf0dce65ac43)



5. *Navigation*:
   - Use the provided buttons to navigate between screens.
   - Deposit money with success
   
   ![Screenshot 2024-12-17 114351](https://github.com/user-attachments/assets/1f49e681-3ed9-4b3b-9728-952d1d973df0)

   - Withdraw money with success
   
   ![Screenshot 2024-12-17 114410](https://github.com/user-attachments/assets/f7f4fb65-80ea-4ebc-94b3-02867a175554)

     
---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   bash
   git checkout -b feature-name
   
3. Commit your changes:
   bash
   git commit -m "Add new feature"
   
4. Push to your branch:
   bash
   git push origin feature-name
   
5. Submit a pull request.

---

## Conclusion

This project provides a simple and functional *Bank Management System* that can be extended further for educational or professional use. It covers basic operations like user management, deposits, and withdrawals with a clean graphical interface.

Feel free to enhance the project with additional features such as *transaction history, **password encryption, or **multi-user support*.

---

# Download My Application

https://drive.google.com/file/d/1kC_UIRhejVG_9liu1yr_l67RUU7LOicd/view?usp=drive_link

*Happy Coding!* 🎉
