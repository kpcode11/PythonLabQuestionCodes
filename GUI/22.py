import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class UserManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("User Management System")
        self.root.geometry("800x600")
        
        # Initialize database
        self.initialize_db()
        
        # Create GUI components
        self.create_widgets()
        
        # Load initial data
        self.load_users()

    def initialize_db(self):
        """Initialize the SQLite database and create table if not exists"""
        self.conn = sqlite3.connect('user_management.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                address TEXT
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        """Create all GUI components"""
        # Main frame
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        tk.Label(self.main_frame, text="User Management System", font=("Arial", 16)).grid(row=0, column=0, columnspan=4, pady=10)
        
        # Entry fields
        tk.Label(self.main_frame, text="Name:").grid(row=1, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.main_frame, width=30)
        self.name_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(self.main_frame, text="Email:").grid(row=2, column=0, sticky=tk.W)
        self.email_entry = tk.Entry(self.main_frame, width=30)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(self.main_frame, text="Phone:").grid(row=3, column=0, sticky=tk.W)
        self.phone_entry = tk.Entry(self.main_frame, width=30)
        self.phone_entry.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.main_frame, text="Address:").grid(row=4, column=0, sticky=tk.W)
        self.address_entry = tk.Entry(self.main_frame, width=30)
        self.address_entry.grid(row=4, column=1, padx=5, pady=5)
        
        # Buttons
        self.add_btn = tk.Button(self.main_frame, text="Add User", command=self.add_user)
        self.add_btn.grid(row=5, column=0, pady=10)
        
        self.update_btn = tk.Button(self.main_frame, text="Update User", command=self.update_user)
        self.update_btn.grid(row=5, column=1, pady=10)
        
        self.delete_btn = tk.Button(self.main_frame, text="Delete User", command=self.delete_user)
        self.delete_btn.grid(row=5, column=2, pady=10)
        
        self.clear_btn = tk.Button(self.main_frame, text="Clear Fields", command=self.clear_fields)
        self.clear_btn.grid(row=5, column=3, pady=10)
        
        # Search
        tk.Label(self.main_frame, text="Search:").grid(row=6, column=0, sticky=tk.W)
        self.search_entry = tk.Entry(self.main_frame, width=30)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)
        self.search_btn = tk.Button(self.main_frame, text="Search", command=self.search_users)
        self.search_btn.grid(row=6, column=2, padx=5)
        
        # Treeview for displaying users
        self.tree = ttk.Treeview(self.main_frame, columns=("ID", "Name", "Email", "Phone", "Address"), show="headings")
        self.tree.grid(row=7, column=0, columnspan=4, pady=10, sticky=tk.NSEW)
        
        # Configure treeview columns
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Address", text="Address")
        
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Phone", width=100)
        self.tree.column("Address", width=200)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=7, column=4, sticky=tk.NS)
        
        # Bind treeview selection
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

    def load_users(self):
        """Load all users from database into treeview"""
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Fetch all users
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        
        # Insert into treeview
        for user in users:
            self.tree.insert("", tk.END, values=user)

    def add_user(self):
        """Add a new user to the database"""
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        
        if not name or not email:
            messagebox.showerror("Error", "Name and Email are required!")
            return
        
        try:
            self.cursor.execute(
                "INSERT INTO users (name, email, phone, address) VALUES (?, ?, ?, ?)",
                (name, email, phone, address)
            )
            self.conn.commit()
            messagebox.showinfo("Success", "User added successfully!")
            self.load_users()
            self.clear_fields()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")

    def update_user(self):
        """Update selected user in the database"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a user to update!")
            return
        
        user_id = self.tree.item(selected_item)['values'][0]
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()
        
        if not name or not email:
            messagebox.showerror("Error", "Name and Email are required!")
            return
        
        try:
            self.cursor.execute(
                "UPDATE users SET name=?, email=?, phone=?, address=? WHERE id=?",
                (name, email, phone, address, user_id)
            )
            self.conn.commit()
            messagebox.showinfo("Success", "User updated successfully!")
            self.load_users()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")

    def delete_user(self):
        """Delete selected user from the database"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a user to delete!")
            return
        
        user_id = self.tree.item(selected_item)['values'][0]
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this user?"):
            self.cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "User deleted successfully!")
            self.load_users()
            self.clear_fields()

    def search_users(self):
        """Search users by name or email"""
        search_term = self.search_entry.get()
        
        # Clear current items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Search in database
        self.cursor.execute(
            "SELECT * FROM users WHERE name LIKE ? OR email LIKE ?",
            (f"%{search_term}%", f"%{search_term}%")
        )
        users = self.cursor.fetchall()
        
        # Insert results into treeview
        for user in users:
            self.tree.insert("", tk.END, values=user)

    def on_tree_select(self, event):
        """Populate entry fields when user is selected in treeview"""
        selected_item = self.tree.selection()
        if selected_item:
            user_data = self.tree.item(selected_item)['values']
            self.clear_fields()
            self.name_entry.insert(0, user_data[1])
            self.email_entry.insert(0, user_data[2])
            self.phone_entry.insert(0, user_data[3])
            self.address_entry.insert(0, user_data[4])

    def clear_fields(self):
        """Clear all entry fields"""
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def __del__(self):
        """Close database connection when object is destroyed"""
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = UserManagementSystem(root)
    root.mainloop()