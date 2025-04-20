import threading
import time

class BankAccount:
    def __init__(self, use_lock=True):
        self.balance = 100  # Initial balance
        self.use_lock = use_lock
        if use_lock:
            self.lock = threading.Lock()
    
    def withdraw(self, amount):
        if self.use_lock:
            with self.lock:
                return self._withdraw(amount)
        else:
            return self._withdraw(amount)
    
    def _withdraw(self, amount):
        # Simulate processing time
        time.sleep(0.1)
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

def customer_action(account, customer_id):
    for attempt in range(10):
        # Check balance (with lock if account uses it)
        if account.use_lock:
            with account.lock:
                current_balance = account.balance
                time.sleep(0.001)  # Simulate decision delay
        else:
            current_balance = account.balance
            time.sleep(0.001)
        
        if current_balance >= 20:
            success = account.withdraw(20)
            if success:
                print(f"Customer-{customer_id} withdrew $20 (Attempt {attempt + 1})")
            else:
                print(f"Customer-{customer_id} - Withdrawal failed (Attempt {attempt + 1})")
        else:
            print(f"Customer-{customer_id} - Insufficient funds (Attempt {attempt + 1})")
            break

def banking_demo(use_lock=True):
    account = BankAccount(use_lock=use_lock)
    
    print("\n" + "="*50)
    print(f"=== {'With Lock' if use_lock else 'Without Lock'} Demo ===")
    print(f"Initial balance: ${account.balance}\n")
    
    customers = [threading.Thread(target=customer_action, args=(account, i)) for i in range(5)]
    
    start_time = time.time()
    for customer in customers:
        customer.start()
    
    for customer in customers:
        customer.join()
    
    duration = time.time() - start_time
    print(f"\nFinal balance: ${account.balance}")
    print(f"Completed in {duration:.2f} seconds")
    print("="*50 + "\n")

if __name__ == "__main__":
    # Run demo without lock first
    print("WARNING: Running without locks will show race condition effects")
    banking_demo(use_lock=False)
    time.sleep(2)
    
    # Then run with proper locking
    print("Running with proper locking:")
    banking_demo(use_lock=True)