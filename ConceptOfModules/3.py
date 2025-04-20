import getpass  # For secure password input
import sys
from datetime import datetime

# Mock user database (in real app, use proper database with hashed passwords)
USER_DB = {
    "admin": {"password": "Admin@123", "attempts": 0, "locked": False},
    "user1": {"password": "Password1!", "attempts": 0, "locked": False},
    "user2": {"password": "Secure#456", "attempts": 0, "locked": False}
}

MAX_ATTEMPTS = 3
LOG_FILE = "login_audit.log"

def write_log(message):
    """Log events to a file with timestamp"""
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f"{datetime.now()} - {message}\n")
    except PermissionError:
        print("Warning: Could not write to log file (permission denied)")
    except Exception as e:
        print(f"Logging error: {type(e).__name__} - {e}")

def login():
    try:
        username = input("Enter username: ").strip()
        
        # Check if user exists
        if username not in USER_DB:
            write_log(f"Login failed - User '{username}' doesn't exist")
            raise KeyError("User doesn't exist")
        
        # Check if account is locked
        if USER_DB[username]["locked"]:
            write_log(f"Login blocked - Account '{username}' is locked")
            raise PermissionError("Account locked (too many failed attempts)")
        
        # Get password securely
        password = getpass.getpass("Enter password: ")
        
        # Validate password
        if password != USER_DB[username]["password"]:
            USER_DB[username]["attempts"] += 1
            write_log(f"Login failed - Incorrect password for '{username}' (Attempt {USER_DB[username]['attempts']})")
            
            if USER_DB[username]["attempts"] >= MAX_ATTEMPTS:
                USER_DB[username]["locked"] = True
                write_log(f"Account '{username}' locked due to too many attempts")
                raise PermissionError("Too many attempts - account locked")
            else:
                raise ValueError("Incorrect password")
        
        # Successful login
        USER_DB[username]["attempts"] = 0  # Reset attempts
        write_log(f"Login successful - User '{username}'")
        return f"Welcome, {username}! Login successful."

    except KeyError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"
    except PermissionError as e:
        return f"Security Error: {e}"
    except Exception as e:
        write_log(f"Unexpected error during login: {type(e).__name__} - {e}")
        return f"System Error: Please try again later"

def main():
    print("\n=== Secure Login System ===")
    while True:
        print("\n1. Login")
        print("2. Exit")
        choice = input("Select option: ")
        
        if choice == '1':
            result = login()
            print(f"\n{result}")
        elif choice == '2':
            print("Exiting system...")
            sys.exit(0)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        sys.exit(1)
    except Exception as e:
        write_log(f"Critical system failure: {type(e).__name__} - {e}")
        print("A critical error occurred. See logs for details.")
        sys.exit(1)