import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# Database setup
def initialize_db():
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Form validation functions
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

def validate_password(password):
    return len(password) >= 8

def validate_username(username):
    return len(username) >= 4 and ' ' not in username

# Main application class
class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Authentication System")
        self.root.geometry("400x300")
        
        # Initialize database
        initialize_db()
        
        # Show login frame by default
        self.show_login_frame()
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def show_login_frame(self):
        self.clear_frame()
        
        # Login Frame
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Username:").pack()
        self.login_username = tk.Entry(self.root)
        self.login_username.pack()
        
        tk.Label(self.root, text="Password:").pack()
        self.login_password = tk.Entry(self.root, show="*")
        self.login_password.pack()
        
        tk.Button(self.root, text="Login", command=self.login_user).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.show_register_frame).pack()
    
    def show_register_frame(self):
        self.clear_frame()
        
        # Registration Frame
        tk.Label(self.root, text="Register", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Username:").pack()
        self.reg_username = tk.Entry(self.root)
        self.reg_username.pack()
        
        tk.Label(self.root, text="Email:").pack()
        self.reg_email = tk.Entry(self.root)
        self.reg_email.pack()
        
        tk.Label(self.root, text="Password:").pack()
        self.reg_password = tk.Entry(self.root, show="*")
        self.reg_password.pack()
        
        tk.Label(self.root, text="Confirm Password:").pack()
        self.reg_confirm_password = tk.Entry(self.root, show="*")
        self.reg_confirm_password.pack()
        
        tk.Button(self.root, text="Register", command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.show_login_frame).pack()
    
    def login_user(self):
        username = self.login_username.get()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()
        
        if user and user[3] == password:  # Simple password check (in real apps, use hashing)
            messagebox.showinfo("Success", "Login successful!")
            # Here you would typically open the main application window
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def register_user(self):
        username = self.reg_username.get()
        email = self.reg_email.get()
        password = self.reg_password.get()
        confirm_password = self.reg_confirm_password.get()
        
        # Validation
        if not all([username, email, password, confirm_password]):
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if not validate_username(username):
            messagebox.showerror("Error", "Username must be at least 4 characters with no spaces")
            return
        
        if not validate_email(email):
            messagebox.showerror("Error", "Invalid email format")
            return
        
        if not validate_password(password):
            messagebox.showerror("Error", "Password must be at least 8 characters")
            return
        
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords don't match")
            return
        
        # Database operation
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)  # In real apps, store hashed password
            )
            conn.commit()
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_frame()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username or email already exists")
        finally:
            conn.close()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()