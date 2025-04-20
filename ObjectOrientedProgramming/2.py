class BankAccount:
    def __init__(self, account_number, name, account_type, balance=0):
        self.account_number = account_number
        self.name = name
        self.account_type = account_type
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("\nInvalid deposit amount!")
    
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"\nWithdrew ₹{amount}. New balance: ₹{self.balance}")
            else:
                print("\nInsufficient funds!")
        else:
            print("\nInvalid withdrawal amount!")
    
    def display_balance(self):
        print(f"\nAccount Balance for {self.name}: ₹{self.balance}")
    
    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.name}\n"
                f"Account Type: {self.account_type}\n"
                f"Balance: ₹{self.balance}\n")

class BankingSystem:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        print("\n--- Create New Account ---")
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account number already exists!")
            return
        
        name = input("Enter account holder name: ")
        account_type = input("Enter account type (Savings/Current): ")
        initial_deposit = float(input("Enter initial deposit amount: ₹"))
        
        if initial_deposit < 0:
            print("Invalid initial deposit amount!")
            return
        
        self.accounts[account_number] = BankAccount(account_number, name, account_type, initial_deposit)
        print("\nAccount created successfully!")
    
    def deposit(self):
        account_number = input("\nEnter account number: ")
        if account_number in self.accounts:
            amount = float(input("Enter deposit amount: ₹"))
            self.accounts[account_number].deposit(amount)
        else:
            print("Account not found!")
    
    def withdraw(self):
        account_number = input("\nEnter account number: ")
        if account_number in self.accounts:
            amount = float(input("Enter withdrawal amount: ₹"))
            self.accounts[account_number].withdraw(amount)
        else:
            print("Account not found!")
    
    def check_balance(self):
        account_number = input("\nEnter account number: ")
        if account_number in self.accounts:
            self.accounts[account_number].display_balance()
        else:
            print("Account not found!")
    
    def show_all_accounts(self):
        print("\n--- All Accounts ---")
        if not self.accounts:
            print("No accounts found!")
        else:
            for account in self.accounts.values():
                print(account)
    
    def run(self):
        while True:
            print("\n==== Banking System ====")
            print("1. Create New Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. Show All Accounts")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                self.show_all_accounts()
            elif choice == '6':
                print("\nThank you for using our banking system!")
                break
            else:
                print("\nInvalid choice! Please try again.")

# Main program
if __name__ == "__main__":
    bank = BankingSystem()
    bank.run()