from flask import Flask, render_template, request, redirect, url_for, flash, session
import random
import pymysql.cursors

app = Flask(__name__)
app.secret_key = 'Bank12'  # Replace with a secure key

# Database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",  # Change to your MySQL password
    database="records",
    cursorclass=pymysql.cursors.DictCursor
)

# Home Page: shows Create Account, Login, and Exit options
@app.route('/')
def home():
    return render_template('home.html')

# Registration page – Create account
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        city = request.form.get('city')
        state = request.form.get('state')
        gender = request.form.get('gender')
        pin = request.form.get('pin')
        # Generate random 12-digit account number
        account_no = random.randint(100000000000, 999999999999)
        # Set initial balance to a random number or 0
        balance = random.choice([0, random.randint(100, 1000)])
        
        if not (name and age and city and state and gender and pin):
            flash("Please fill all fields.", "danger")
            return redirect(url_for('register'))
        
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO New_User (name, age, city, state, gender, pin, balance, account_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, (name, int(age), city, state, gender, int(pin), balance, account_no))
            connection.commit()
            flash(f"Your account is created! Your account number is: {account_no} and initial balance is: ₹{balance}", "success")
            return redirect(url_for('home'))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('register'))
    return render_template('register.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        pin = request.form.get('pin')
        if not (name and pin):
            flash("Please fill all fields.", "danger")
            return redirect(url_for('login'))
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM New_User WHERE name=%s AND pin=%s"
                cursor.execute(sql, (name, int(pin)))
                user = cursor.fetchone()
            if user:
                session['user'] = user
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials.", "danger")
                return redirect(url_for('login'))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')

# Dashboard page – shows balance and options for deposit, withdraw, delete account, or exit (logout)
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('login'))
    user = session['user']
    return render_template('dashboard.html', user=user)

# Deposit page
@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if 'user' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = request.form.get('amount')
        if not (amount and amount.isdigit() and int(amount) > 0):
            flash("Please enter a valid amount.", "danger")
            return redirect(url_for('deposit'))
        amount = int(amount)
        user = session['user']
        new_balance = user['balance'] + amount
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE New_User SET balance=%s WHERE account_no=%s"
                cursor.execute(sql, (new_balance, user['account_no']))
            connection.commit()
            # Update session value
            user['balance'] = new_balance
            session['user'] = user
            flash(f"₹{amount} has been deposited successfully! New Balance: ₹{new_balance}", "success")
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('deposit'))
    return render_template('deposit.html')

# Withdraw page
@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if 'user' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('login'))
    if request.method == 'POST':
        amount = request.form.get('amount')
        if not (amount and amount.isdigit() and int(amount) > 0):
            flash("Please enter a valid amount.", "danger")
            return redirect(url_for('withdraw'))
        amount = int(amount)
        user = session['user']
        if amount > user['balance']:
            flash("Insufficient balance.", "danger")
            return redirect(url_for('dashboard'))
        new_balance = user['balance'] - amount
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE New_User SET balance=%s WHERE account_no=%s"
                cursor.execute(sql, (new_balance, user['account_no']))
            connection.commit()
            user['balance'] = new_balance
            session['user'] = user
            flash(f"₹{amount} has been withdrawn successfully! Remaining Balance: ₹{new_balance}", "success")
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f"Error: {str(e)}", "danger")
            return redirect(url_for('withdraw'))
    return render_template('withdraw.html')

# Delete account route
@app.route('/delete', methods=['POST'])
def delete():
    if 'user' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('login'))
    user = session['user']
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM New_User WHERE account_no=%s"
            cursor.execute(sql, (user['account_no'],))
        connection.commit()
        flash("Your account has been deleted.", "success")
        session.pop('user', None)
        return redirect(url_for('home'))
    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for('dashboard'))

# Logout route
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully.", "info")
    return redirect(url_for('home'))

# Exit App
@app.route('/exit')
def exit_app():
    return render_template('exit.html')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return "Shutting down..."

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10000)

