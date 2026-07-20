import tkinter as tk  
from tkinter import messagebox  
import sqlite3  

# Connect to SQLite database (or create it)  
conn = sqlite3.connect('banking_system.db')  
cursor = conn.cursor()  

# Create a table for bank accounts  
cursor.execute('''  
CREATE TABLE IF NOT EXISTS accounts (  
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,  
    username TEXT NOT NULL UNIQUE,  
    password TEXT NOT NULL,  
    balance REAL NOT NULL DEFAULT 0  
)  
''')  

cursor.execute('''  
CREATE TABLE IF NOT EXISTS transactions (  
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,  
    account_id INTEGER,  
    amount REAL,  
    transaction_type TEXT,  
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  
    FOREIGN KEY (account_id) REFERENCES accounts (account_id)  
)  
''')  
conn.commit()  

# Functions for banking operations  
def create_account():
    username = entry_username.get()  
    password = entry_password.get()  
    
    try:  
        cursor.execute('INSERT INTO accounts (username, password) VALUES (?, ?)', (username, password))  
        conn.commit()  
        messagebox.showinfo("Success", "Account created successfully!")  
    except sqlite3.IntegrityError:  
        messagebox.showerror("Error", "Username already exists!")  

def login():  
    username = entry_username.get()  
    password = entry_password.get()  
    
    cursor.execute('SELECT * FROM accounts WHERE username=? AND password=?', (username, password))  
    account = cursor.fetchone()  
    
    if account:  
        messagebox.showinfo("Success", "Login successful!")  
        open_account_window(account[0], username)  
    else:  
        messagebox.showerror("Error", "Invalid credentials!")  

def open_account_window(account_id, username):  
    def deposit():  
        amount = float(entry_amount.get())  
        cursor.execute('UPDATE accounts SET balance = balance + ? WHERE account_id = ?', (amount, account_id))  
        cursor.execute('INSERT INTO transactions (account_id, amount, transaction_type) VALUES (?, ?, ?)', (account_id, amount, 'deposit'))  
        conn.commit()  
        messagebox.showinfo("Success", f"{amount} deposited successfully!")  
        check_balance()  

    def withdraw():  
        amount = float(entry_amount.get())  
        cursor.execute('SELECT balance FROM accounts WHERE account_id = ?', (account_id,))  
        balance = cursor.fetchone()[0]  
        if balance >= amount:  
            cursor.execute('UPDATE accounts SET balance = balance - ? WHERE account_id = ?', (amount, account_id))  
            cursor.execute('INSERT INTO transactions (account_id, amount, transaction_type) VALUES (?, ?, ?)', (account_id, amount, 'withdrawal'))  
            conn.commit()  
            messagebox.showinfo("Success", f"{amount} withdrawn successfully!")  
        else:  
            messagebox.showerror("Error", "Insufficient balance!")  
        check_balance()  

    def check_balance():  
        cursor.execute('SELECT balance FROM accounts WHERE account_id = ?', (account_id,))  
        balance = cursor.fetchone()[0]  
        label_balance.config(text=f"Balance: {balance}")  

    def view_transactions():  
        cursor.execute('SELECT * FROM transactions WHERE account_id = ?', (account_id,))  
        transactions = cursor.fetchall()  
        transaction_history = "\n".join([f"{row[4]}: {row[2]} ({row[3]})" for row in transactions])  
        messagebox.showinfo("Transaction History", transaction_history if transaction_history else "No transactions found.")  
    
    # Create a new window for account operations  
    account_window = tk.Toplevel(root)  
    account_window.title("Account Operations")  
    
    label_balance = tk.Label(account_window, text="Balance: 0")  
    label_balance.pack()  
    
    label_amount = tk.Label(account_window, text="Enter amount:")  
    label_amount.pack()  
    
    entry_amount = tk.Entry(account_window)  
    entry_amount.pack()  
    
    button_deposit = tk.Button(account_window, text="Deposit", command=deposit)  
    button_deposit.pack()  
    
    button_withdraw = tk.Button(account_window, text="Withdraw", command=withdraw)  
    button_withdraw.pack()  
    
    button_check_balance = tk.Button(account_window, text="Check Balance", command=check_balance)  
    button_check_balance.pack()  
    
    button_view_transactions = tk.Button(account_window, text="View Transactions", command=view_transactions)  
    button_view_transactions.pack()  
    
    check_balance()  # Display initial balance  

# Main Application Window  
root = tk.Tk()  
root.title("ATM Banking System")  
root.geometry('400x400')

label_username = tk.Label(root, text="Username:")  
label_username.pack()  

entry_username = tk.Entry(root)  
entry_username.pack()  

label_password = tk.Label(root, text="Password:")  
label_password.pack()  

entry_password = tk.Entry(root, show='*')  
entry_password.pack()  

button_create_account = tk.Button(root, text="Create Account", command=create_account)  
button_create_account.pack()  

button_login = tk.Button(root, text="Login", command=login)  
button_login.pack()  

root.mainloop()  
 
conn.close()