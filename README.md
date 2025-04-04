# 🏦 Bank Management System

A full-stack **Flask-based web application** for managing bank user accounts — allowing user registration, login, deposits, withdrawals, balance checks, and account deletion. This app uses **MySQL** for data storage.

![image](https://github.com/user-attachments/assets/d1f5e5f8-9992-4129-a9a4-e3fee8932e90)

---

## 🔧 Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Python, Flask
- **Database**: MySQL (via PyMySQL)

---

## 🚀 Features

- 🧾 **User Registration** with random account number & initial balance  
- 🔐 **Secure Login** using username and PIN  
- 💼 **Dashboard** with current balance and banking operations  
- 💰 **Deposit & Withdraw** money with session-based balance update  
- ❌ **Delete Account** functionality  
- 🚪 **Logout & Exit Pages**   
- 🖼️ Background image support and UI enhancements 

---

## 📁 Project Structure

bank-management/ 

├── templates/ │

  ├── home.html │ 
  
  ├── login.html │
  
  ├── register.html │ 
  
  ├── dashboard.html │
  
  ├── deposit.html │ └── withdraw.html

  ├── exit.html
  
├── app.py # Main Flask application file
  
├── requirements.txt # Python dependencies
  
└── README.md
  
---

## 🛠️ Setup Instructions

### ✅ Prerequisites

 Python 3.7+
 
 MySQL Server installed and running

 Git (optional)

---

### 📦 2. Create Virtual Environment & Install Dependencies

pip install -r requirements.txt


### 🗄️ 3. Configure MySQL Database

#### 1. Start MySQL and login:

mysql -u root -p

#### 2. Run the following SQL to create DB & table:

CREATE DATABASE records;

USE records;

CREATE TABLE New_User (
 
    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100),

    age INT,

    city VARCHAR(100),

    state VARCHAR(100),

    gender VARCHAR(10),

    pin INT,

    balance INT,

    account_no BIGINT
    
);

#### Update the DB connection in app.py:

 connection = pymysql.connect(

     host="localhost",

     user="root",

     password="your_mysql_password",

     database="records",

     cursorclass=pymysql.cursors.DictCursor
     
)
#### ▶️ 4. Run the Flask App

python app.py

Visit http://localhost:5000 in your browser.

## 📸 Screenshots 
Add screenshots in a screenshots/ folder and display them here:

### Home Page	Dashboard
![Screenshot 2025-04-05 004703](https://github.com/user-attachments/assets/dd8f3d64-dd67-4a31-a918-c3de02edcc6e)

### Create New Account and its Result Pages
![Screenshot 2025-04-05 004758](https://github.com/user-attachments/assets/91c00192-d1ce-42ce-80b0-97edde69db1b)

![Screenshot 2025-04-05 004825](https://github.com/user-attachments/assets/bf1d9ce4-f715-4a2a-a355-d3c882fc88bf)

### Login Page
![Screenshot 2025-04-05 004851](https://github.com/user-attachments/assets/76f354a1-33b9-4532-9e54-b3ab3b759407)

### Login Dashboard
![Screenshot 2025-04-05 004907](https://github.com/user-attachments/assets/3807a308-d4ef-4952-aa4d-7185d21e21a0)

### Deposit Page
![Screenshot 2025-04-05 004933](https://github.com/user-attachments/assets/1dd23310-ad45-4c7b-8962-866d227c41a3)

### Withdraw Page
![Screenshot 2025-04-05 005011](https://github.com/user-attachments/assets/1ba4ba67-e36f-485c-845c-97de6ea0defd)

### Results of Deposit, Withdraw and Delete
![Screenshot 2025-04-05 005049](https://github.com/user-attachments/assets/bb5da5f8-4a01-4853-8b74-bd1bde5f33d7)

### Exit
![Screenshot 2025-04-05 005101](https://github.com/user-attachments/assets/249c8e2a-a412-4f24-9fa9-26553d2c462f)

## 🤝 Contributing
Feel free to fork this repository, improve the project, and submit a pull request!

## 🤝 Author
Nishant Kumar
🎓 Data Scientist | 💻 Python, SQL, ML, Flask

## 📬 Contact
Nishant Kumar
📧 your: nitin1412003@gmail.com
🔗 [Linkedin](https://www.linkedin.com/in/nishant-kumar-b55951285/)

