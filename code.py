import tkinter as tk
from tkinter import messagebox
import random
import pymysql.cursors

# Database connection
connection = pymysql.connect(
    host="localhost",
    user='root',
    password="password",  
    cursorclass=pymysql.cursors.DictCursor,
    database="bank_management" 
)
mycursor = connection.cursor()

# Functions for navigating the UI
def show_main_menu():
    new_user_frame.pack_forget()
    login_user_frame.pack_forget()
    transaction_frame.pack_forget()
    deposit_frame.pack_forget()
    withdraw_frame.pack_forget()
    main_menu_frame.pack()

def show_new_user():
    main_menu_frame.pack_forget()
    new_user_frame.pack()

def show_login_user():
    main_menu_frame.pack_forget()
    login_user_frame.pack()

def show_transaction():
    login_user_frame.pack_forget()
    transaction_frame.pack()

def show_deposit():
    transaction_frame.pack_forget()
    deposit_frame.pack()

def show_withdraw():
    transaction_frame.pack_forget()
    withdraw_frame.pack()

# Function to create a new user
def create_new_user():
    name = name_entry.get()
    age = age_entry.get()
    pin = pin_entry.get()
    state = state_entry.get()
    gender = gender_entry.get()
    account_no = random.randint(10000000000, 99999999999)

    if not (name and age and pin and state and gender):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        mycursor.execute(
            "INSERT INTO New_User (name, age, pin, state, gender, balance, account_no) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, int(age), int(pin), state, gender, 0, account_no)
        )
        connection.commit()
        messagebox.showinfo("Success", "New user created successfully!\nAccount No: " + str(account_no))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to log in as an existing user
def login_user():
    global logged_in_user
    name = login_name_entry.get()
    pin = login_pin_entry.get()

    if not (name and pin):
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        mycursor.execute("SELECT * FROM New_User WHERE name = %s AND pin = %s", (name, int(pin)))
        user = mycursor.fetchone()

        if user:
            logged_in_user = user
            balance_label.config(text=f"Current Balance: ₹{logged_in_user['balance']}")
            show_transaction()
        else:
            messagebox.showerror("Error", "Invalid credentials.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to deposit money
def deposit_money():
    amount = deposit_entry.get()

    if not amount or not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    new_balance = logged_in_user['balance'] + int(amount)
    try:
        mycursor.execute("UPDATE New_User SET balance = %s WHERE account_no = %s", (new_balance, logged_in_user['account_no']))
        connection.commit()
        logged_in_user['balance'] = new_balance
        balance_label.config(text=f"Current Balance: ₹{new_balance}")
        messagebox.showinfo("Success", f"Deposited ₹{amount} successfully!")
        show_main_menu()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to withdraw money
def withdraw_money():
    amount = withdraw_entry.get()

    if not amount or not amount.isdigit() or int(amount) <= 0:
        messagebox.showerror("Error", "Please enter a valid amount.")
        return

    if int(amount) > logged_in_user['balance']:
        messagebox.showerror("Error", "Insufficient balance.")
        return

    new_balance = logged_in_user['balance'] - int(amount)
    try:
        mycursor.execute("UPDATE New_User SET balance = %s WHERE account_no = %s", (new_balance, logged_in_user['account_no']))
        connection.commit()
        logged_in_user['balance'] = new_balance
        balance_label.config(text=f"Current Balance: ₹{new_balance}")
        messagebox.showinfo("Success", f"Withdrawn ₹{amount} successfully!")
        show_main_menu()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to delete a user's account
def delete_account():
    global logged_in_user

    if not logged_in_user:
        messagebox.showerror("Error", "No user is logged in.")
        return

    confirm = messagebox.askyesno("Delete Account", "Are you sure you want to delete your account? This action cannot be undone.")
    
    if confirm:
        try:
            mycursor.execute("DELETE FROM New_User WHERE account_no = %s", (logged_in_user['account_no'],))
            connection.commit()

            # Clear the logged in user and return to the main menu
            logged_in_user = None
            messagebox.showinfo("Success", "Your account has been deleted.")
            show_main_menu()  # Return to the main menu
        except Exception as e:
            messagebox.showerror("Error", str(e))


# Tkinter setup
root = tk.Tk()
root.title("Bank Management System")
root.geometry("400x400")

logged_in_user = None

# Main Menu Frame
main_menu_frame = tk.Frame(root, bg="lightblue")
main_menu_frame.pack(fill="both", expand=True)

tk.Label(main_menu_frame, text="Bank Management System", font=("Arial", 16), bg="lightblue").pack(pady=20)

tk.Button(main_menu_frame, text="New User", font=("Arial", 12), bg="green", fg="white", activebackground="darkgreen", activeforeground="white", command=show_new_user).pack(pady=10)
tk.Button(main_menu_frame, text="Login User", font=("Arial", 12), bg="orange", fg="white", activebackground="darkorange", activeforeground="white", command=show_login_user).pack(pady=10)
tk.Button(main_menu_frame, text="Exit", font=("Arial", 12), bg="red", fg="white", activebackground="darkred", activeforeground="white", command=root.destroy).pack(pady=10)

# New User Frame
new_user_frame = tk.Frame(root, bg="lightyellow")

name_label = tk.Label(new_user_frame, text="Name:", bg="lightyellow")
name_label.pack()
name_entry = tk.Entry(new_user_frame)
name_entry.pack()

age_label = tk.Label(new_user_frame, text="Age:", bg="lightyellow")
age_label.pack()
age_entry = tk.Entry(new_user_frame)
age_entry.pack()

pin_label = tk.Label(new_user_frame, text="PIN:", bg="lightyellow")
pin_label.pack()
pin_entry = tk.Entry(new_user_frame, show="*")
pin_entry.pack()

state_label = tk.Label(new_user_frame, text="State:", bg="lightyellow")
state_label.pack()
state_entry = tk.Entry(new_user_frame)
state_entry.pack()

gender_label = tk.Label(new_user_frame, text="Gender:", bg="lightyellow")
gender_label.pack()
gender_entry = tk.Entry(new_user_frame)
gender_entry.pack()

tk.Button(new_user_frame, text="Create User", bg="green", fg="white", activebackground="darkgreen", activeforeground="white", command=create_new_user).pack(pady=10)
tk.Button(new_user_frame, text="Back to Main Menu", bg="gray", fg="white", activebackground="darkgray", activeforeground="white", command=show_main_menu).pack(pady=10)

# Login User Frame
login_user_frame = tk.Frame(root, bg="lightpink")

login_name_label = tk.Label(login_user_frame, text="Name:", bg="lightpink")
login_name_label.pack()
login_name_entry = tk.Entry(login_user_frame)
login_name_entry.pack()

login_pin_label = tk.Label(login_user_frame, text="PIN:", bg="lightpink")
login_pin_label.pack()
login_pin_entry = tk.Entry(login_user_frame, show="*")
login_pin_entry.pack()

tk.Button(login_user_frame, text="Login", bg="blue", fg="white", activebackground="darkblue", activeforeground="white", command=login_user).pack(pady=10)
tk.Button(login_user_frame, text="Back to Main Menu", bg="gray", fg="white", activebackground="darkgray", activeforeground="white", command=show_main_menu).pack(pady=10)

# Transaction Frame
transaction_frame = tk.Frame(root, bg="lightgreen")

tk.Label(transaction_frame, text="Transaction Menu", font=("Arial", 16), bg="lightgreen").pack(pady=10)

balance_label = tk.Label(transaction_frame, text="", font=("Arial", 12), bg="lightgreen")
balance_label.pack(pady=10)

tk.Button(transaction_frame, text="Deposit", bg="purple", fg="white", activebackground="brown", activeforeground="white", command=show_deposit).pack(pady=5)
tk.Button(transaction_frame, text="Withdraw", bg="purple", fg="white", activebackground="brown", activeforeground="white", command=show_withdraw).pack(pady=5)
tk.Button(transaction_frame, text="Back to Main Menu", bg="gray", fg="white", activebackground="purple", activeforeground="white", command=show_main_menu).pack(pady=10)
tk.Button(transaction_frame, text="Delete Account", bg="red", fg="white", activebackground="darkred", activeforeground="white", command=delete_account).pack(pady=5)

# Deposit Frame
deposit_frame = tk.Frame(root, bg="lightblue")

tk.Label(deposit_frame, text="Deposit Amount:", bg="lightblue").pack()
deposit_entry = tk.Entry(deposit_frame)
deposit_entry.pack()
tk.Button(deposit_frame, text="Confirm Deposit", bg="green", fg="white", activebackground="darkgreen", activeforeground="white", command=deposit_money).pack(pady=5)
tk.Button(deposit_frame, text="Back to Transaction Menu", bg="gray", fg="white", activebackground="darkgray", activeforeground="white", command=show_transaction).pack(pady=10)

# Withdraw Frame
withdraw_frame = tk.Frame(root, bg="lightcoral")

tk.Label(withdraw_frame, text="Withdraw Amount:", bg="lightcoral").pack()
withdraw_entry = tk.Entry(withdraw_frame)
withdraw_entry.pack()
tk.Button(withdraw_frame, text="Confirm Withdraw", bg="red", fg="white", activebackground="darkred", activeforeground="white", command=withdraw_money).pack(pady=5)
tk.Button(withdraw_frame, text="Back to Transaction Menu", bg="gray", fg="white", activebackground="darkgray", activeforeground="white", command=show_transaction).pack(pady=10)

# Start the application
root.mainloop()
